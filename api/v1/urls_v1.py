# api/v1/urls_v1.py
from django.urls import path
from api.v1 import views

urlpatterns = [
    # Category Views
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # Product Views
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Ingredient Views
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/create/', views.ingredient_create, name='ingredient_create'),
    path('ingredients/<int:pk>/', views.ingredient_detail, name='ingredient_detail'),
    path('ingredients/<int:pk>/update/', views.ingredient_update, name='ingredient_update'),
    path('ingredients/<int:pk>/delete/', views.ingredient_delete, name='ingredient_delete'),
    
    # Recipe Views
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/create/', views.recipe_create, name='recipe_create'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/update/', views.recipe_update, name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    
    # Order Views
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    
    # OrderItem Views
    path('orderitems/', views.orderitem_list, name='orderitem_list'),
    path('orderitems/create/', views.orderitem_create, name='orderitem_create'),
    path('orderitems/<int:pk>/', views.orderitem_detail, name='orderitem_detail'),
    path('orderitems/<int:pk>/update/', views.orderitem_update, name='orderitem_update'),
    path('orderitems/<int:pk>/delete/', views.orderitem_delete, name='orderitem_delete'),
    
    # DeliveryCompany Views
    path('deliverycompanies/', views.deliverycompany_list, name='deliverycompany_list'),
    path('deliverycompanies/create/', views.deliverycompany_create, name='deliverycompany_create'),
    path('deliverycompanies/<int:pk>/', views.deliverycompany_detail, name='deliverycompany_detail'),
    path('deliverycompanies/<int:pk>/update/', views.deliverycompany_update, name='deliverycompany_update'),
    path('deliverycompanies/<int:pk>/delete/', views.deliverycompany_delete, name='deliverycompany_delete'),
]