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
            'data_urls': {},
            'data_attrs': {},
        }


class Home(ReactView):

    def get_context_data(self, **kwargs):
        return {
            'title': "Home",
            'bundle': 'books',
            'data_urls': [
                ('books', reverse('twyla_api:books-list')),
                ('rates', reverse('twyla_api:rates-list')),
            ]
        }


class BookList(ReactView):

    def get_context_data(self, **kwargs):
        return {
            'title': "Book List",
            'bundle': 'books-list',
            'data_urls': [
                ('books', reverse('twyla_api:books-list')),
                ('rates', reverse('twyla_api:rates-list')),
            ]
        }


class BookReview(ReactView):
    title = "Book Review"

    def get_context_data(self, **kwargs):
        return {
            'title': "Book Review",
            'bundle': 'books-review',
            'data_urls': [
                ('books', reverse('twyla_api:books-list')),
                ('rates', reverse('twyla_api:rates-list')),
            ],
            'data_attrs': [
                ('book-id', kwargs.get('book_id', None)),
            ]
        }


class BookCreate(ReactView):

    def get_context_data(self, **kwargs):
        return {
            'title': "Book Create",
            'bundle': 'books-create',
            'data_urls': [
                ('books', reverse('twyla_api:books-list')),
                ('rates', reverse('twyla_api:rates-list')),
            ]
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
        if form.is_valid():
            form.save()
            return self._perform_login(request)
        else:
            return self._perform_login(request)

        return render(request, self.template_name, {'form': form})

    def _perform_login(request):
            user = get_user_model().objects.filter(
                username=request.POST['username'],
            ).first()
            login(request, user)
            response = HttpResponseRedirect('/home')
            response.set_cookie('username', user.username)
            return response

    def _redirect_if_authenticated(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/home')
