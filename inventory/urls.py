from django.urls import path
from .views import home, inventory

urlpatterns = [
    path('', home, name='home'),
    path('inventory/', inventory, name='inventory'),
]