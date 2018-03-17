from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from project.apps.twyla.api.serializers import BookSerializer, RateSerializer
from project.apps.twyla.models import Book, Rate
from django.db.models import Q
from project.pagination import BasePaginator


class BookViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Book.objects.filter(
            created_by=self.request.user
        ).order_by('-id')


class RateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    serializer_class = RateSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Rate.objects.filter(
            Q(created_by=self.request.user) |
            Q(
                book__created_by=self.request.user,
            )
        ).order_by('-id')
