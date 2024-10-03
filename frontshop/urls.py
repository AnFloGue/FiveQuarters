# frontshop/urls.py
from django.urls import path
from .views import inventory_information

urlpatterns = [
    path('backshop-information/', inventory_information, name='inventory_information'),

]