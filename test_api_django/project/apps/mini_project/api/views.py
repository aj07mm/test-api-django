from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from project.apps.mini_project.api.serializers import ProfileSerializer
from project.apps.mini_project.models import Profile
from project.pagination import BasePaginator


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProfileSerializer
    pagination_class = BasePaginator
    queryset = Profile.objects.all()
