from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        return user
