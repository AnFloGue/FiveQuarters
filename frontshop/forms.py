# frontshop/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']