from django import forms
from project.apps.restaurants.models import Profile

class ProfileForm(forms.ModelForm):
    read_only = ('uuid',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'u-full-width'

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'current_position', 'about_you', 'topics')
        exclude = ['user', 'uuid']
