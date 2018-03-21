from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        return {
            'title': "Home",
            'bundle': 'books',
            'data_urls': [
                #('books', reverse('spa_api:books-list')),
                #('rates', reverse('spa_api:rates-list')),
            ],
            'data_attrs': {},
        }


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
