# frontshop/views.py


import jwt
from datetime import datetime, timedelta
import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from backshop.models import Product
from frontshop.services.read_services import (
    get_recommended_products,
    get_category_list,
    get_product_list,
    get_deliverycompany_list,
    get_order_list,
    get_ingredient_list,
    product_full_list,
    product_full_detail,
    get_account_list,
    get_account_details,
    get_user_profile_list,
    get_user_profile_details,
    get_order_details,
    get_orderitem_list,
    get_orderitem_details,
    get_deliverycompany_details,
    get_category_details,
    get_product_details,
    get_ingredient_details,
    get_recipe_list,
    get_recipe_details
)
from django.conf import settings
from django.urls import reverse
import requests

API_BASE_URL = settings.API_BASE_URL_V1
JWT_SECRET = settings.SECRET_KEY  # Use your secret key for JWT encoding
JWT_ALGORITHM = 'HS256'

logging.basicConfig(
    filename='logs/django_errors.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s'
)

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1),  # Token expiration time
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

# ================================================
# Home Views
# ================================================




@login_required
def home(request):
    if request.user.is_authenticated:
        logging.info("User is successfully logged in.")
    else:
        logging.info("User is not logged in.")

    # Check for the JWT token (e.g., stored in a cookie)
    token = request.COOKIES.get('jwt_token')

    if not token:
        # Log the failure and redirect to login if no token is found
        logging.info("No JWT token found. Redirecting to login.")
        return redirect('login')

    # Make API requests with the token in the header
    headers = {'Authorization': f'Bearer {token}'}
    products = requests.get(f"{API_BASE_URL}/product-full-list/", headers=headers).json()
    recommended_products = requests.get(
        f"{API_BASE_URL}/product-full-list/", headers=headers
    ).json()[:3]

    context = {
        'products': products,
        'recommended_products': recommended_products,
    }
    return render(request, 'frontshop/home.html', context)

# ================================================
# Product Views
# ================================================
@login_required
def product_list(request):
    # Check for the JWT token
    token = request.COOKIES.get('jwt_token')
    if not token:
        return redirect('login')

    headers = {'Authorization': f'Bearer {token}'}

    products = requests.get(f"{API_BASE_URL}/products/", headers=headers).json()
    categories = requests.get(
        f"{API_BASE_URL}/categories/", headers=headers
    ).json()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'frontshop/product_list.html', context)


@login_required
def product_detail(request, product_id):
    # Check for the JWT token
    token = request.COOKIES.get('jwt_token')
    if not token:
        return redirect('login')

    headers = {'Authorization': f'Bearer {token}'}

    categories = requests.get(
        f"{API_BASE_URL}/categories/", headers=headers
    ).json()
    products = requests.get(f"{API_BASE_URL}/products/", headers=headers).json()
    ingredients = requests.get(
        f"{API_BASE_URL}/ingredients/", headers=headers
    ).json()
    product_details = requests.get(
        f"{API_BASE_URL}/product-full-list/", headers=headers
    ).json()
    products_with_ingredients = requests.get(
        f"{API_BASE_URL}/product-full-detail/{product_id}/", headers=headers
    ).json()

    # Get the specific product and its availability status
    product = next(
        (p for p in products if p['id'] == product_id), None
    )  # Find product in the list
    if not product:
        return HttpResponseRedirect(
            reverse('product_list')
        )  # Redirect if product not found

    context = {
        'categories': categories,
        'products': products,
        'ingredients': ingredients,
        'product_details': product_details,
        'products_with_ingredients': products_with_ingredients,
        'product': product,
        'is_available': product['is_available'],
    }

    return render(request, 'frontshop/product_detail.html', context)


# ================================================
# inventory_information Views
# ================================================
@login_required
def inventory_information(request):
    # Implementation for inventory information view
    return render(request, 'frontshop/inventory_information.html')


# ================================================
# Order Product Views
# ================================================
@login_required
def order_product(request, product_id):
    # Implementation for order product view
    return render(request, 'frontshop/order_product.html')


@login_required
def order_summary(request, product_id, amount):
    # Implementation for order summary view
    return render(request, 'frontshop/order_summary.html')


# ================================================
# Login, Register, Logout Views
# ================================================

# Configure logging
logging.basicConfig(
    filename='/Users/antoniofloresguerrero/PycharmProjects/_FINAL PROJ/#01/FiveQuarters/logs/django_errors.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
                logging.error('Login failed: Invalid username or password for user %s', username)
        else:
            logging.error('Login form is invalid: %s', form.errors)
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

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# ================================================
# Other Views (about, submit_review)
# ================================================
@login_required
def about(request):
    # Implementation for about view
    return render(request, 'frontshop/about.html')


@login_required
def submit_review(request, product_id):
    # Implementation for submit review view
    return render(request, 'frontshop/submit_review.html')