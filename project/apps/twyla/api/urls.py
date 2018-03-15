from rest_framework import routers
from project.apps.twyla.api import views


router = routers.DefaultRouter()
router.register(r'books', views.ProfileViewSet, base_name="books")
router.register(r'rates', views.ProfileViewSet, base_name="rates")

urlpatterns = router.urls
