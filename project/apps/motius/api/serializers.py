from django.urls import reverse
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from project.apps.motius.models import Article



class ArticleSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Article
        fields = "__all__"

    def to_representation(self, request_data):
        # get the original representation
        ret = super(ArticleSerializer, self).to_representation(request_data)
        current_user = self.context['request'].user
        for field_name, field_value in sorted(ret.items()):
            if not current_user.has_perm(
                'motius.read_{}_article'.format(field_name)
            ):
                ret.pop(field_name)

        return ret

    def to_internal_value(self, request_data):
        # get the original representation
        ret = super(ArticleSerializer, self).to_representation(request_data)
        current_user = self.context['request'].user
        for field_name, field_value in sorted(ret.items()):
            if field_value and not current_user.has_perm(
                'motius.change_{}_article'.format(field_name)
            ):
                raise ValidationError({
                    field_name: ["Field not allowed to change"]
                })

        return ret
