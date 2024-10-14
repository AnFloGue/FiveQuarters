# frontshop/urls.py
from django.urls import path
from .views import (
    home, about, login_view, register_view, logout_view,
    product_list, product_detail, inventory_information,
    order_product, submit_review, basketitem_list, add_to_basket,
)

urlpatterns = [
    
    # ================================================
    # Login, Register, Logout Views
    # ================================================
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),
    
    
    # ================================================
    # Frontshop Views
    # ================================================

    path('home/', home, name='home'),
    
    # ================================================
    # Product Views
    # ================================================
    
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('product_list/', product_list, name='product_list'),
    
    # ================================================
    # Order Product Views
    # ================================================
    
    path('order/<int:product_id>/', order_product, name='order_product'),

    path('inventory-information/', inventory_information, name='inventory_information'),
    
    # ================================================
    # basketitem Views
    # ================================================
    
    path('basket/', basketitem_list, name='basketitem_list'),
    path('add-to-basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    
    # ================================================
    # About View
    # ================================================
    path('about/', about, name='about'),

]