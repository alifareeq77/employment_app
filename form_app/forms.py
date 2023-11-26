from django import forms

from form_app.models import Form


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'description']


class PaymentOptionForm(forms.Form):
    plan = forms.CharField(label='Choose Your Payment Plan:', required=True, widget=forms.RadioSelect(choices=(
        ('six-months', '6'),
        ('three-months', '3'),
    )))
