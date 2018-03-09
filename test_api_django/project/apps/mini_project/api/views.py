from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from project.apps.mini_project.api.serializers import ProfileSerializer
from project.apps.mini_project.models import Profile
from project.pagination import BasePaginator


class ProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProfileSerializer
    pagination_class = BasePaginator
    queryset = Profile.objects.all()
