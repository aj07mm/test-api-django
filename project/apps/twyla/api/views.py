from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from project.apps.twyla.api.serializers import BookSerializer, RateSerializer
from project.apps.twyla.models import Book
from project.pagination import BasePaginator


class BookViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)

    serializer_class = BookSerializer
    pagination_class = BasePaginator
    queryset = Book.objects.all()


class RateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)

    serializer_class = RateSerializer
    pagination_class = BasePaginator
    queryset = Rate.objects.all()
