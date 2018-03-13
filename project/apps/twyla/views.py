from django.shortcuts import render
from django.contrib.auth import login, get_user_model
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from project.apps.twyla.forms import LoginForm


class Home(TemplateView):
    template_name = "home.html"

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
            return HttpResponseRedirect('/home')
        else:
            login(request, get_user_model().objects.filter(username=request.POST['username']).first()) # if created, log in
            return HttpResponseRedirect('/home')

        return render(request, self.template_name, {'form': form})

    def _redirect_if_authenticated(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/home')
