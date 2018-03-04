from django import forms
from project.apps.restaurants.models import Profile

class ProfileForm(forms.ModelForm):
    read_only = ('uuid',)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'current_position', 'about_you', 'topics')
        exclude = ['user', 'uuid']
