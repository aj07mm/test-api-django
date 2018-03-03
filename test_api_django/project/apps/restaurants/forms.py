from django import forms
from project.apps.restaurants.models import Profile

class ProfileForm(forms.ModelForm):
    read_only = ('uuid',)
    class Meta:
        model = Profile
        fields = ('user', 'name', 'position', 'description', 'topics')
