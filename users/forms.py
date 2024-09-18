from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=72)
    password = forms.CharField(max_length=72, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']