from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from project.apps.restaurants.models import Restaurant
from project.apps.restaurants.serializers import RestaurantSerializer
from project.apps.restaurants.forms import ProfileForm
from project.pagination import BasePaginator


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = RestaurantSerializer
    pagination_class = BasePaginator
    queryset = Restaurant.objects.all()

def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
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
