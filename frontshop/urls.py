# frontshop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order-items/', views.order_item_list, name='order_item_list'),
    path('order-items/<int:order_item_id>/', views.order_item_detail, name='order_item_detail'),
]