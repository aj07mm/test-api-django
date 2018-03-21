from rest_framework import routers
from project.apps.spa_app.api import views

app_name = 'spa_app'
router = routers.DefaultRouter()
#router.register(r'books', views.BookViewSet, base_name="books")
#router.register(r'rates', views.RateViewSet, base_name="rates")

urlpatterns = router.urls
