import factory
from django.contrib.auth.models import User
from project.apps.restaurants.models import Profile


class UserFactory(factory.Factory):
    class Meta:
        model = User

class ProfileFactory(factory.Factory):
    class Meta:
        model = Profile
