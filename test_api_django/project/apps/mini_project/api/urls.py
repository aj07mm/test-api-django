from rest_framework import routers
from project.apps.mini_project.api import views


router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, base_name="profiles")

urlpatterns = router.urls
