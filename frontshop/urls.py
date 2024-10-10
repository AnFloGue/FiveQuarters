# frontshop/urls.py
from django.urls import path
from .views import (
    home,
    about,
    inventory_information,
    login_view,
    register_view,
    logout_view,
    product_list,
    product_detail,
    
)

urlpatterns = [
    
# ================================================
# Home, Product List, Product Detail URLs
# ================================================
    
    path('home/', home, name='home'),
    
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    
    path('product_list/', product_list, name='product_list'),
    
    
# ================================================
# Inventory Information, About URLs
# ================================================
    path('inventory-information/', inventory_information, name='inventory_information'),
    
    path('about/', about, name='about'),
    
    # ================================================
# Login, Register, Logout URLs
# ================================================
    
    path('login/', login_view, name='login'),
    
    path('register/', register_view, name='register'),
    
    path('logout/', logout_view, name='logout'),
]