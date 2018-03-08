from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404
from project.apps.mini_project.forms import ProfileForm, UserForm
from project.apps.mini_project.models import Profile
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class Home(TemplateView):
    template_name = "home.html"


class Profiles(TemplateView):
    template_name = "registration/profiles.html"

    def get_context_data(self, **kwargs):
        return {
            'bundle': 'profiles',
            'profiles': Profile.objects.all(),
        }


class ProfileDetail(TemplateView):
    template_name = "registration/profile.html"

    def get_context_data(self, **kwargs):
        id = kwargs.get('profile_id')
        if id:
            profile = get_object_or_404(Profile, pk=id)
            profile_form = ProfileForm(instance=profile)
        else:
            profile_form = ProfileForm()

        return {
            'is_user_page': profile.user == self.request.user,
            'profile_form': profile_form,
            'topics': self.request.user.profile.get_topics_ordered(profile),
        }

    def post(self, request, *args, **kwargs):
        id = kwargs.get('profile_id')
        profile = get_object_or_404(Profile, pk=id)
        profile_form = ProfileForm(self.request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

        return render(
            request,
            self.template_name,
            {
                'is_user_page': profile.user == self.request.user,
                'profile_form': profile_form,
                'topics': self.request.user.profile.get_topics_ordered(profile),
            }
        )


def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            # user_form
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login and redirect
            login(request, user)
            return HttpResponseRedirect(
                reverse('profile_detail', args=[user.profile.uuid])
            )
    else:
        user_form = UserForm()

    return render(
        request,
        'registration/signup.html',
        {
            'user_form': user_form,
        }
    )
