from django.contrib import admin
from project.apps.restaurants.models import (
    Topic,
    User,
    Profile,
)

admin.site.register(Topic)
# admin.site.register(User)
admin.site.register(Profile)
