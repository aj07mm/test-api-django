from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

admin.autodiscover()


urlpatterns = [
    path('', RedirectView.as_view(url='/admin/'), name='home'),
    path('admin/', admin.site.urls),
    # path('api/', include('project.apps.foobar.urls')),
]
