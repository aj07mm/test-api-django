from django.contrib import admin
from django.contrib.auth.models import Permission
from project.apps.motius.models import Article

admin.autodiscover()

admin.site.register(Article)
admin.site.register(Permission)
