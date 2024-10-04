# frontshop/urls.py
# frontshop/urls.py
from django.urls import path
from .views import inventory_information, create_order_view

urlpatterns = [
    path('inventory-information/', inventory_information, name='inventory_information'),
    path('create_order/', create_order_view, name='create_order'),
]