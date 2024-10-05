# frontshop/views.py
from django.shortcuts import render, redirect
from .read_services import (
    get_category_list,
    get_product_list,
    get_deliverycompany_list,
    get_order_list
)
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page or dashboard
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'frontshop/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
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

    context = {
        'categories': categories,
        'products': products,
        'delivery_companies': delivery_companies,
        'orders': orders,
    }

    return render(request, 'frontshop/inventory-information.html', context)











# def order_detail(request):
#     return render(request, 'frontshop/order_detail.html')
#
# def order_item_detail(request):
#     return render(request, 'frontshop/order_item_detail.html')
#
# def order_item_list(request):
#     return render(request, 'frontshop/order_item_list.html')
#
# def order_list(request):
#     return render(request, 'frontshop/order_list.html')