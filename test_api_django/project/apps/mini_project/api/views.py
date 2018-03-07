from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from project.apps.mini_project.models import Profile
from project.apps.mini_project.api.serializers import ProfileSerializer
from project.apps.mini_project.forms import ProfileForm, UserForm
from project.apps.mini_project.models import Profile
from project.pagination import BasePaginator
from django.views.generic import TemplateView
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse


class ProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProfileSerializer
    pagination_class = BasePaginator
    queryset = Profile.objects.all()
