from django import forms

from form_app.models import Form


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'description']