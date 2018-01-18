from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from project.apps.restaurants import views


router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

urlpatterns = router.urls
