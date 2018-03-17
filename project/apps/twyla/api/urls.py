from rest_framework import routers
from project.apps.twyla.api import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet, base_name="books")
router.register(r'rates', views.RateViewSet, base_name="rates")

urlpatterns = router.urls
