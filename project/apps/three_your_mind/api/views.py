from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from project.apps.three_your_mind import serializers
from project.apps.three_your_mind.models import Printer
from project.pagination import BasePaginator


class BookViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PrinterSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Printer.objects.all()
