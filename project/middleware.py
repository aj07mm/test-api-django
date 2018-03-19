from django.utils.deprecation import MiddlewareMixin
from project.apps.twyla.utils import set_current_user


class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        set_current_user(getattr(request, 'user', None))
