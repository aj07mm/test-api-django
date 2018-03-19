import factory
from project.apps.twyla.models import Rate, Book, User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User


class BookFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Book


class RateFactory(factory.django.DjangoModelFactory):
    book = factory.SubFactory(BookFactory)

    class Meta:
        model = Rate
