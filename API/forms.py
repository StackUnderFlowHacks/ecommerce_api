from django import forms
from .models import Details


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('name', 'email', 'password', 'phone')
        widgets = {'password': forms.PasswordInput()}
