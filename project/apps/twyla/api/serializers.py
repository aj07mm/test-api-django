from rest_framework import serializers
from django.urls import reverse
from project.apps.twyla.models import Book, Rate


class BookSerializer(serializers.ModelSerializer):
    review_book_url = serializers.SerializerMethodField(read_only=True)

    class Meta(object):
        model = Book
        fields = "__all__"

    def get_review_book_url(self, obj):
        return reverse('review_book', kwargs={'book_id': obj.id})


class RateSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Rate
        fields = "__all__"
