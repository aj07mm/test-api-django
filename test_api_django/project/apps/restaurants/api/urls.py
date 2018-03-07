from rest_framework import routers
from project.apps.restaurants.api import views


router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = router.urls
