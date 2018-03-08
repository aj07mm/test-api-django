from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from project.apps.mini_project.models import Profile

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class ProfileForm(BaseForm):
    read_only = ('uuid',)

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'current_position',
            'about_you',
            'topics',
        )
        exclude = ['user', 'uuid']


class UserForm(UserCreationForm, BaseForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'
