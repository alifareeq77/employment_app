from django import forms
from .models import CustomUser
from .models import Appliers, Owner


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    type = forms.ChoiceField(choices=(("owner", "form owner"), ("applier", 'form applier')))

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'type']

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


class ApplierForm(forms.ModelForm):
    class Meta:
        model = Appliers
        fields = ['first_name', 'last_name']


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name']
