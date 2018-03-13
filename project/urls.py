from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from project.apps.twyla import views

urlpatterns = (
    url(r'^$', RedirectView.as_view(url='/home')),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^login/?$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^$', RedirectView.as_view(url='/api')),
    #url(
    #    r'^api/',
    #    include('project.apps.foobar.urls', namespace='foobar')
    #),
    url(r'^admin/', admin.site.urls),
)
