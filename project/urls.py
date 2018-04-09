from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView

from project import settings


admin.autodiscover()


urlpatterns = [
    url(r'^foo/', include(('project.apps.data_incubator.urls', 'data_incubator'))),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
