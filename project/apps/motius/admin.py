from django.contrib import admin
from project.apps.motius.models import Article

admin.autodiscover()

admin.site.register(Article)
