from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from project.apps.restaurants import views
from django.contrib.auth.decorators import login_required

admin.autodiscover()


urlpatterns = (
    url(r'^$', RedirectView.as_view(url='/home')),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(
        r'^profiles/(?P<profile_id>[0-9a-f-]+)/$',
        login_required(views.ProfileDetail.as_view()),
        name='profile_detail'
    ),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(
        r'^api/',
        include('project.apps.restaurants.urls', namespace='restaurants')
    ),
)
