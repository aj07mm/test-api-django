from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from project.apps.motius.api.serializers import ArticleSerializer
from project.apps.motius.models import Article
from project.pagination import BasePaginator


class ArticleViewSet(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    serializer_class = ArticleSerializer
    pagination_class = BasePaginator
    queryset = Article.objects.all()
