from rest_framework import routers
from project.apps.three_your_mind import views

router = routers.DefaultRouter()
router.register(r'printers', views.BookViewSet, base_name="printers")

urlpatterns = router.urls
