from rest_framework import routers
from project.apps.motius.api import views

app_name = 'motius'
router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet, "articles")

urlpatterns = router.urls
