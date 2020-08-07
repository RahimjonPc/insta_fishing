from .models import Fishing
from django.forms import ModelForm, TextInput


class FishingForm(ModelForm):
    class Meta:
        model = Fishing
        fields = ["username", "password"]
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username or phone number'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
        }