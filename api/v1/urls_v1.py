# api/v1/urls_v1.py
from django.urls import path
from api.v1 import views
from .views import (
    register, login, product_full_list, product_full_detail
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    # Auth Views
    path('register/', register, name='register'),
    path('login/', login, name='login'),

    # Token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Account Views
    path('accounts/', views.account_list, name='account_list'),
    path('accounts/create/', views.create_account, name='create_account'),
    path('accounts/<int:pk>/', views.account_detail, name='account_detail'),
    path('accounts/<int:pk>/update/', views.update_account, name='update_account'),
    path('accounts/<int:pk>/delete/', views.delete_account, name='delete_account'),

    # UserProfile Views
    path('userprofiles/', views.user_profile_list, name='user_profile_list'),
    path('userprofiles/create/', views.create_user_profile, name='create_user_profile'),
    path('userprofiles/<int:pk>/', views.user_profile_detail, name='user_profile_detail'),
    path('userprofiles/<int:pk>/update/', views.update_user_profile, name='update_user_profile'),
    path('userprofiles/<int:pk>/delete/', views.delete_user_profile, name='delete_user_profile'),

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
    path('product-full-list/', product_full_list, name='product_full_list'),
    path('product-full-detail/<int:pk>/', product_full_detail, name='product_full_detail'),

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

    # Basket Views
    path('baskets/', views.basket_list, name='basket_list'),
    path('baskets/create/', views.basket_create, name='basket_create'),
    path('baskets/<int:pk>/', views.basket_detail, name='basket_detail'),
    path('baskets/<int:pk>/update/', views.basket_update, name='basket_update'),
    path('baskets/<int:pk>/delete/', views.basket_delete, name='basket_delete'),

    # BasketItem Views
    path('basketitems/', views.basketitem_list, name='basketitem_list'),
    path('basketitems/create/', views.basketitem_create, name='basketitem_create'),
    path('basketitems/<int:pk>/', views.basketitem_detail, name='basketitem_detail'),
    path('basketitems/<int:pk>/update/', views.basketitem_update, name='basketitem_update'),
    path('basketitems/<int:pk>/delete/', views.basketitem_delete, name='basketitem_delete'),

    # Allergen Views
    path('allergens/', views.allergen_list, name='allergen_list'),
    path('allergens/create/', views.allergen_create, name='allergen_create'),
    path('allergens/<int:pk>/', views.allergen_detail, name='allergen_detail'),
    path('allergens/<int:pk>/update/', views.allergen_update, name='allergen_update'),
    path('allergens/<int:pk>/delete/', views.allergen_delete, name='allergen_delete'),
]