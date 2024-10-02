# api/v1/urls_v1.py
from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:order_id>/', views.get_order_details, name='order_detail'),
    path('orders/<int:order_id>/items/', views.orderitem_list_by_order, name='order_item_list_by_order'),
]