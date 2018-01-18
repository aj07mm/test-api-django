from django.contrib import admin
from django.conf.urls import include, url


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = (
    # Admin panel and documentation:
    url(r'^admin/', admin.site.urls),
)
