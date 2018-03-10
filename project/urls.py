from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView

admin.autodiscover()


urlpatterns = (
    url(r'^$', RedirectView.as_view(url='/api')),
    url(r'^admin/', admin.site.urls),
    #url(
    #    r'^api/',
    #    include('project.apps.foobar.urls', namespace='foobar')
    #),
)
