from rest_framework import viewsets
from project.apps.restaurants.models import Restaurant
from project.apps.restaurants.serializers import RestaurantSerializer
from project.pagination import BasePaginator


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = RestaurantSerializer
    pagination_class = BasePaginator
    queryset = Restaurant.objects.all()
