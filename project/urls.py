from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from project.apps.spa_app import views as spa_app_views



urlpatterns = (
    url(r'^$', spa_app_views.Home.as_view(), name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    url(r'^signup/$', spa_app_views.signup, name='signup'),
    url(
        r'^api/',
        include('project.apps.spa_app.api.urls', namespace='spa_api')
    ),
)
