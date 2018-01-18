from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter
from project.apps.restaurants import urls

admin.autodiscover()


urlpatterns = (
    # Admin panel and documentation:
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('project.apps.restaurants.urls', namespace='restaurants')),
)
