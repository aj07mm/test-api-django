from django.contrib import admin
from project.apps.mini_project.models import (
    Topic,
    User,
    Profile,
)


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Topic)
#admin.site.register(Profile)
