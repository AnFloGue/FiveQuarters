# frontshop/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .read_services import (
    get_category_list,
    get_product_list,
    get_deliverycompany_list,
    get_order_list,
    get_ingredient_list,
)
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

from django import forms



# ================================================
# Home Views
# ================================================



def home(request):
    products = get_product_list()
    categories = get_category_list()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'frontshop/home.html', context)

# ================================================
# Login, Register, Logout Views
# ================================================

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inventory_information')  # Redirect to a home page or dashboard
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'frontshop/login.html', {'form': form})

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'frontshop/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# ================================================
# inventory_information Views
# ================================================

def inventory_information(request):
    categories = get_category_list()
    products = get_product_list()
    delivery_companies = get_deliverycompany_list()
    orders = get_order_list()
    ingredients = get_ingredient_list()


    context = {
        'categories': categories,
        'products': products,
        'delivery_companies': delivery_companies,
        'orders': orders,
        'ingredients': ingredients,
    }

    return render(request, 'frontshop/inventory-information.html', context)