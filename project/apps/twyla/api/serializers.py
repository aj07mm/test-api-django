from rest_framework import serializers
from django.urls import reverse
from project.apps.twyla.models import Book, Rate, User



class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ("username",)
        read_only_fields = ('created_by',)


class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    review_book_url = serializers.SerializerMethodField(read_only=True)

    class Meta(object):
        model = Book
        fields = "__all__"
        read_only_fields = ('created_by',)

    def get_review_book_url(self, obj):
        return reverse('book_review', kwargs={'book_id': obj.id})


class RateSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta(object):
        model = Rate
        fields = "__all__"
        read_only_fields = ('created_by',)
