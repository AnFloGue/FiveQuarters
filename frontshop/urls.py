# frontshop/urls.py
from django.urls import path
from .views import (
    home,
    inventory_information,
    login_view,
    register_view,
    logout_view,
    product_list

)

urlpatterns = [
    path('inventory-information/', inventory_information, name='inventory_information'),


    path('home/', home, name='home'),
    
    path('product_list/', product_list, name='product_list'),
    
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]