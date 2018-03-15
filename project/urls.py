from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from project.apps.twyla import views

urlpatterns = (
    url(r'^$', RedirectView.as_view(url='/home')),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^add_book/$', views.AddBook.as_view(), name='add_book'),
    url(r'^add_rate/$', views.AddRate.as_view(), name='add_rate'),

    # auth
    url(r'^login/?$', views.Login.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', RedirectView.as_view(url='/api')),
    url(
        r'^api/',
        include('project.apps.twyla.api.urls', namespace='api')
    ),
)
