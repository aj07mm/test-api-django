from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from project.apps.restaurants.models import Restaurant
from project.apps.restaurants.serializers import RestaurantSerializer
from project.apps.restaurants.forms import ProfileForm
from project.apps.restaurants.models import Profile
from project.pagination import BasePaginator
from django.views.generic import TemplateView
from django.http import HttpResponseForbidden, HttpResponseRedirect


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = RestaurantSerializer
    pagination_class = BasePaginator
    queryset = Restaurant.objects.all()


class Home(TemplateView):
    template_name = "home.html"


class ProfileDetail(TemplateView):
    template_name = "registration/profile.html"

    def get_context_data(self, **kwargs):
        id = kwargs.get('profile_id')
        if id:
            profile = get_object_or_404(Profile, pk=id)
            self.profile = profile
            if profile.user != self.request.user:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()

        profile_form = ProfileForm(instance=profile)
        return {
            'profile_form': profile_form,
        }

    def post(self, request, *args, **kwargs):
        id = kwargs.get('profile_id')
        profile = get_object_or_404(Profile, pk=id)
        profile_form = ProfileForm(self.request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
        return render(request, self.template_name, {'profile_form': profile_form})

def signup(request):

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # user_form
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # profile_form
            user_form.save()
            # login and redirect
            login(request, user)
            return redirect('/')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()

    return render(
        request,
        'registration/signup.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    )
