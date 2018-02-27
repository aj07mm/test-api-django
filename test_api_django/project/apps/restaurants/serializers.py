from rest_framework import serializers
from project.apps.restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Restaurant
        fields = (
            'id',
            'name',
            'opens_at',
            'closes_at',
        )
