from rest_framework import serializers
from project.apps.twyla.models import Book, Rate


class BookSerializer(serializers.ModelSerializer):
    book_url = serializers.SerializerMethodField(read_only=True)

    class Meta(object):
        model = Book
        fields = "__all__"

    def get_book_url(self, obj):
        return ''
        #return reverse('book_detail', kwargs={'book_id': obj.uuid})


class RateSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Rate
        fields = "__all__"
