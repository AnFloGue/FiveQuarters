# frontshop/forms.py

from django import forms
from django.contrib.auth.models import User


# ================================================
# LoginForm, RegisterForm
# ================================================

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        
        return cleaned_data

# ================================================
# update_basketitem form
# ================================================

class UpdateBasketItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')