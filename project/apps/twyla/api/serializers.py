from rest_framework import serializers
from django.core.urlresolvers import reverse
from project.apps.twyla.models import Book, Rate


class BookSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Book
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Rate
        fields = "__all__"
