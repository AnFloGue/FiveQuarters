# frontshop/views.py

from .models import Product

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import LoginForm, RegisterForm
import logging
from frontshop.services.read_services import (
    get_recommended_products,
    get_category_list,
    get_product_list,
    get_deliverycompany_list,
    get_order_list,
    get_ingredient_list,
    product_full_list,
    product_full_detail,
    get_basketitem_list,
    get_basketitem_detail,

)

from frontshop.services.create_services import (
    create_order,
    create_order_item,
)

# Configure logging
logging.basicConfig(
    filename='/Users/antoniofloresguerrero/PycharmProjects/_FINAL PROJ/#01/FiveQuarters/logs/django_errors.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ================================================
# Home Views
# ================================================

@login_required
def home(request):
    products = get_product_list()
    recommended_products = get_recommended_products()[:3]

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
    products = get_product_list()
    categories = get_category_list()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'frontshop/product_list.html', context)

@login_required
def product_detail(request, product_id):
    categories = get_category_list()
    products = get_product_list()
    ingredients = get_ingredient_list()
    product_details = product_full_list()
    products_with_ingredients = product_full_detail(product_id)

    # Get the specific product and its availability status
    product = get_object_or_404(Product, id=product_id)

    context = {
        'categories': categories,
        'products': products,
        'ingredients': ingredients,
        'product_details': product_details,
        'products_with_ingredients': products_with_ingredients,
        'product': product,
        'is_available': product.is_available,
    }

    return render(request, 'frontshop/product_detail.html', context)

# ================================================
# Inventory Information Views
# ================================================

@login_required
def inventory_information(request):
    categories = get_category_list()
    products = get_product_list()
    delivery_companies = get_deliverycompany_list()
    orders = get_order_list()
    ingredients = get_ingredient_list()
    product_details = product_full_list()
    products_with_ingredients = product_full_detail(2)

    context = {
        'categories': categories,
        'products': products,
        'delivery_companies': delivery_companies,
        'orders': orders,
        'ingredients': ingredients,
        'product_details': product_details,
        'products_with_ingredients': products_with_ingredients
    }

    return render(request, 'frontshop/inventory-information.html', context)

# ================================================
# Orders Views
# ================================================


# views.py
@login_required
def order_product(request, product_id):
 pass
    
# ================================================
# Basket Views
# ================================================




@login_required
def basketitem_list(request):
    user = request.user
    basketitems = get_basketitem_list(user)

    # Extract basket information from the first basket item
    if basketitems:
        basket = {
            'id': basketitems[0]['basket'],
            'created_at': basketitems[0].get('created_at', ''),
            'updated_at': basketitems[0].get('updated_at', ''),
        }
    else:
        basket = None

    context = {
        'basket': basket,
        'basketitems': basketitems,
    }
    return render(request, 'frontshop/basket_summary.html', context)


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
                logging.info(f"Login successful for user: {username}")
                return redirect(reverse('home'))
            else:
                form.add_error(None, 'Invalid username or password')
                logging.warning(f"Login failed for user: {username}")
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
            logging.info(f"Registration successful for user: {user.username}")
            return redirect('login')
        else:
            logging.warning("Registration failed due to invalid form data")
    else:
        form = RegisterForm()
    return render(request, 'frontshop/register.html', {'form': form})

@login_required
def logout_view(request):
    username = request.user.username
    logout(request)
    logging.info(f"Logout successful for user: {username}")
    return redirect('login')

# ================================================
# Other Views
# ================================================


def about(request):
    return render(request, 'frontshop/about.html')

def submit_review(request):
    return render(request, 'frontshop/about.html')