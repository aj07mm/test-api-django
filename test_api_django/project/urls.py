from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from project.apps.mini_project import views
from django.contrib.auth.decorators import login_required
from project.apps.mini_project.forms import MyAuthenticationForm


admin.autodiscover()


urlpatterns = (
    url(r'^$', RedirectView.as_view(url='/home')),
    url(r'^home/$', views.Home.as_view(), name='home'),

    # registration
    url(r'^signup/$', views.signup, name='signup'),
    url(
        r'^login/?$',
        auth_views.login,
        {
            'template_name': 'registration/login.html',
            'authentication_form': MyAuthenticationForm
        },
        name="login"
    ),
    url(r'^logout/$', auth_views.logout, name='logout'),

    # profiles
    url(
        r'^user/(?P<profile_id>[0-9a-f-]+)/$',
        login_required(views.ProfileDetail.as_view()),
        name='profile_detail'
    ),
    url(
        r'^user/$',
        login_required(views.Profiles.as_view()),
        name='profiles'
    ),
    url(
        r'^api/',
        include(
            'project.apps.mini_project.api.urls',
            namespace='api_profile'
        )
    ),
    url(r'^admin/', admin.site.urls),
)
