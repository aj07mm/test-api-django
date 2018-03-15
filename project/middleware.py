import time
from importlib import import_module

from django.conf import settings
from django.contrib.sessions.backends.base import UpdateError
from django.core.exceptions import SuspiciousOperation
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import http_date
from django.contrib import auth
from django.utils.functional import SimpleLazyObject

from django.contrib.sessions.backends.db import SessionStore as DbSessionStore


class SessionStore(DbSessionStore):
    def cycle_key(self):
        super(SessionStore, self).cycle_key()
        self.save()

# https://github.com/django/django/blob/master/django/contrib/auth/__init__.py
#def get_user(request):
#    """
#    Return the user model instance associated with the given request session.
#    If no user is retrieved, return an instance of `AnonymousUser`.
#    """
#    from .models import AnonymousUser
#    user = None
#    try:
#        user_id = _get_user_session_key(request)
#        backend_path = request.session[BACKEND_SESSION_KEY]
#    except KeyError:
#        pass
#    else:
#        if backend_path in settings.AUTHENTICATION_BACKENDS:
#            backend = load_backend(backend_path)
#            user = backend.get_user(user_id)
#            # Verify the session
#            if hasattr(user, 'get_session_auth_hash'):
#                session_hash = request.session.get(HASH_SESSION_KEY)
#                session_hash_verified = session_hash and constant_time_compare(
#                    session_hash,
#                    user.get_session_auth_hash()
#                )
#                if not session_hash_verified:
#                    request.session.flush()
#                    user = None
#
#    return user or AnonymousUser()


def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE%s setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.user = SimpleLazyObject(lambda: get_user(request))


class SessionMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response
        engine = import_module(settings.SESSION_ENGINE)
        self.SessionStore = engine.SessionStore

    def process_request(self, request):
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        request.session = self.SessionStore(session_key)

    def process_response(self, request, response):
        """
        If request.session was modified, or if the configuration is to save the
        session every time, save the changes and set a session cookie or delete
        the session cookie if the session has been emptied.
        """
        try:
            accessed = request.session.accessed
            modified = request.session.modified
            empty = request.session.is_empty()
        except AttributeError:
            pass
        else:
            # First check if we need to delete this cookie.
            # The session should be deleted only if the session is entirely empty
            if settings.SESSION_COOKIE_NAME in request.COOKIES and empty:
                response.delete_cookie(
                    settings.SESSION_COOKIE_NAME,
                    path=settings.SESSION_COOKIE_PATH,
                    domain=settings.SESSION_COOKIE_DOMAIN,
                )
            else:
                if accessed:
                    patch_vary_headers(response, ('Cookie',))
                if (modified or settings.SESSION_SAVE_EVERY_REQUEST) and not empty:
                    if request.session.get_expire_at_browser_close():
                        max_age = None
                        expires = None
                    else:
                        max_age = request.session.get_expiry_age()
                        expires_time = time.time() + max_age
                        expires = http_date(expires_time)
                    # Save the session data and refresh the client cookie.
                    # Skip session save for 500 responses, refs #3881.
                    if response.status_code != 500:
                        try:
                            request.session.save()
                        except UpdateError:
                            raise SuspiciousOperation(
                                "The request's session was deleted before the "
                                "request completed. The user may have logged "
                                "out in a concurrent request, for example."
                            )
                        response.set_cookie(
                            settings.SESSION_COOKIE_NAME,
                            #request.session.session_key,
                            request.user.username,
                            max_age=max_age,
                            expires=expires,
                            domain=settings.SESSION_COOKIE_DOMAIN,
                            path=settings.SESSION_COOKIE_PATH,
                            secure=settings.SESSION_COOKIE_SECURE or None,
                            httponly=settings.SESSION_COOKIE_HTTPONLY or None,
                        )
        return response


#class UserCookieMiddleWare(object):
#    """
#    Middleware to set user cookie
#    If user is authenticated and there is no cookie, set the cookie,
#    If the user is not authenticated and the cookie remains, delete it
#    """
#
#    def __init__(self, get_response):
#        self.get_response = get_response
#
#    def __call__(self, request):
#        return self.get_response(request)
#
#    def process_response(self, request, response):
#        #if user and no cookie, set cookie
#        if request.user.is_authenticated() and not request.COOKIES.get('username'):
#            response.set_cookie("username", request.user.username)
#        elif not request.user.is_authenticated() and request.COOKIES.get('username'):
#            #else if if no user and cookie remove user cookie, logout
#            response.delete_cookie("username")
#        return response
