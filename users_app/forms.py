from django import forms
from .models import Appliers


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Appliers
        exclude = ('updated_at', 'created_at', 'user')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return password2


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',

    )
    password = forms.CharField()
