from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from project.apps.twyla.api import serializers
from project.apps.twyla.models import Book, Rate
from django.db.models import Q
from project.pagination import BasePaginator


class BookViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BookSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        created_by__id = self.request.GET.get('created_by__id', None)
        if created_by__id:
            return Book.objects.filter(
                created_by__id=created_by__id,
            ).order_by('-id')
        return Book.objects.all()


class RateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    pagination_class = BasePaginator

    def get_queryset(self):
        '''
            reviews she wrote,
            in addition to the reviews others wrote for the books she added
        '''
        return Rate.objects.filter(
            Q(created_by=self.request.user) |
            Q(
                book__created_by=self.request.user,
            )
        ).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.RateCreateSerializer
        return serializers.RateListSerializer
