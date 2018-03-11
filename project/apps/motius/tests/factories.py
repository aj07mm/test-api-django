import factory
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from project.apps.motius.models import Article
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class PermissionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Permission


class ContentTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ContentType


class GroupFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Group

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Article
