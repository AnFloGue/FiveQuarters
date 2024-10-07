# frontshop/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from frontshop.services.read_services import (
    get_category_list,
    get_product_list,
    get_deliverycompany_list,
    get_order_list,
    get_ingredient_list,
)
from datetime import date


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
# Product Views
# ================================================

def product_list(request):
    products = get_product_list()
    categories = get_category_list()
    today = date.today()
    context = {
        'products': products,
        'categories': categories,
        'today': today,
    }
    return render(request, 'frontshop/product_list.html', context)

# ================================================
# Login, Register, Logout Views
# ================================================

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'frontshop/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'frontshop/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




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

def about(request):
    return render(request, 'frontshop/about.html')