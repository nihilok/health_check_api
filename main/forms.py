from django import forms
from .models import User, HealthCheck
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['NHS_no', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class HealthCheckForm(forms.ModelForm):

    class Meta:
        model = HealthCheck
        fields = ['age', 'height', 'weight', 'smoking', 'alcohol']
        help_texts = {
            'age': 'How old are you in years?',
            'height': 'Your height in centimetres.',
            'weight': 'Your weight in kilograms.',
            'smoking': 'How many cigarettes do you smoke per day?',
            'alcohol': 'How many units of alcohol do you consume per week?',
        }