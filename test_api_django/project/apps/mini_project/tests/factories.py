import factory
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from project.apps.mini_project.models import Profile, Topic


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(
        'project.apps.mini_project.tests.factories.UserFactory',
        profile=None,
    )

    class Meta:
        model = Profile


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    profile = factory.RelatedFactory(ProfileFactory, 'user')

    class Meta:
        model = User


class TopicFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Topic
