from rest_framework import serializers
from django.urls import reverse
from project.apps.motius.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Article
        fields = "__all__"
