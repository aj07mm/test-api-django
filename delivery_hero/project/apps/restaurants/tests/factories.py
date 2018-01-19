import factory
from project.apps.restaurants.models import Restaurant


class RestaurantFactory(factory.Factory):
    class Meta:
        model = Restaurant
