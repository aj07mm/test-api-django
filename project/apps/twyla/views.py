from django.shortcuts import render
from django.contrib.auth import login, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from project.apps.twyla.forms import LoginForm


class ReactView(TemplateView):
    template_name = "react_view.html"

    def get_context_data(self, **kwargs):
        return {
            'bundle': None,
            'data_url': None,
        }


class Home(ReactView):

    def get_context_data(self, **kwargs):
        return {
            'bundle': 'books',
            'data_url_books': reverse('twyla_api:books-list'),
            'data_url_rates': reverse('twyla_api:rates-list'),
        }


class BookReview(ReactView):

    def get_context_data(self, **kwargs):
        return {
            'bundle': 'books-review',
            'data_url': reverse('twyla_api:books-list'),
        }

class BookCreate(ReactView):

    def get_context_data(self, **kwargs):
        return {
            'bundle': 'books-review',
            'data_url': reverse('twyla_api:books-list'),
        }


class AddRate(ReactView):

    def get_context_data(self, **kwargs):
        return {
            'bundle': 'rates',
            'data_url': reverse('twyla_api:rates-list'),
        }


class Login(TemplateView):
    template_name = "login.html"
    initial = {'key': 'value'}
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        self._redirect_if_authenticated(request)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        self._redirect_if_authenticated(request)
        form = self.form_class(request.POST)
        if form.is_valid(): # if don't exist create
            form.save()
            user = get_user_model().objects.filter(username=request.POST['username']).first()
            login(request, user) # if created, log in
            response = HttpResponseRedirect('/home')
            response.set_cookie('username', user.username)
            return response
        else:
            user = get_user_model().objects.filter(username=request.POST['username']).first()
            login(request, user) # if created, log in
            response = HttpResponseRedirect('/home')
            response.set_cookie('username', user.username)
            return response

        return render(request, self.template_name, {'form': form})

    def _redirect_if_authenticated(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/home')
