# api/v1/urls_v1.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

# Auth Views
from api.v1.views.auth_views import register, login

# Account Views
from api.v1.views.account_views import (
    account_list, create_account, account_detail, update_account, delete_account,
    user_profile_list, create_user_profile, user_profile_detail, update_user_profile, delete_user_profile
)

# Product Views
from api.v1.views.product_views import (
    category_list, category_create, category_detail, category_update, category_delete,
    product_list, product_create, product_detail, product_update, product_delete,
    product_full_list, product_full_detail,
    ingredient_list, ingredient_create, ingredient_detail, ingredient_update, ingredient_delete,
    recipe_list, recipe_create, recipe_detail, recipe_update, recipe_delete,
    allergen_list, allergen_create, allergen_detail, allergen_update, allergen_delete, product_create
)

# Basket Views
from api.v1.views.basket_views import (
    basket_list, basket_create, basket_detail, basket_update, basket_delete,
    basketitem_list, basketitem_create, basketitem_detail, basketitem_update, basketitem_delete
)

# Order Views
from api.v1.views.order_views import (
    order_list, order_create, order_detail, order_update, order_delete,
    orderitem_list, orderitem_create, orderitem_detail, orderitem_update, orderitem_delete,
    deliverycompany_list, deliverycompany_create, deliverycompany_detail, deliverycompany_update, deliverycompany_delete
)

urlpatterns = [
    # Auth Views
    path('register/', register, name='register'),
    path('login/', login, name='login'),

    # Token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Account Views
    path('accounts/', account_list, name='account_list'),
    path('accounts/create/', create_account, name='create_account'),
    path('accounts/<int:pk>/', account_detail, name='account_detail'),
    path('accounts/<int:pk>/update/', update_account, name='update_account'),
    path('accounts/<int:pk>/delete/', delete_account, name='delete_account'),

    # UserProfile Views
    path('userprofiles/', user_profile_list, name='user_profile_list'),
    path('userprofiles/create/', create_user_profile, name='create_user_profile'),
    path('userprofiles/<int:pk>/', user_profile_detail, name='user_profile_detail'),
    path('userprofiles/<int:pk>/update/', update_user_profile, name='update_user_profile'),
    path('userprofiles/<int:pk>/delete/', delete_user_profile, name='delete_user_profile'),


    # Category Views
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('categories/<int:pk>/update/', category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),
    
    # Product Views
    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    path('product-full-list/', product_full_list, name='product_full_list'),
    path('product-full-detail/<int:pk>/', product_full_detail, name='product_full_detail'),

    # Ingredient Views
    path('ingredients/', ingredient_list, name='ingredient_list'),
    path('ingredients/create/', ingredient_create, name='ingredient_create'),
    path('ingredients/<int:pk>/', ingredient_detail, name='ingredient_detail'),
    path('ingredients/<int:pk>/update/', ingredient_update, name='ingredient_update'),
    path('ingredients/<int:pk>/delete/', ingredient_delete, name='ingredient_delete'),

    # Recipe Views
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/create/', recipe_create, name='recipe_create'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/update/', recipe_update, name='recipe_update'),
    path('recipes/<int:pk>/delete/', recipe_delete, name='recipe_delete'),

    # Order Views
    path('orders/', order_list, name='order_list'),
    path('orders/create/', order_create, name='order_create'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
    path('orders/<int:pk>/update/', order_update, name='order_update'),
    path('orders/<int:pk>/delete/', order_delete, name='order_delete'),

    # OrderItem Views
    path('orderitems/', orderitem_list, name='orderitem_list'),
    path('orderitems/create/', orderitem_create, name='orderitem_create'),
    path('orderitems/<int:pk>/', orderitem_detail, name='orderitem_detail'),
    path('orderitems/<int:pk>/update/', orderitem_update, name='orderitem_update'),
    path('orderitems/<int:pk>/delete/', orderitem_delete, name='orderitem_delete'),

    # DeliveryCompany Views
    path('deliverycompanies/', deliverycompany_list, name='deliverycompany_list'),
    path('deliverycompanies/create/', deliverycompany_create, name='deliverycompany_create'),
    path('deliverycompanies/<int:pk>/', deliverycompany_detail, name='deliverycompany_detail'),
    path('deliverycompanies/<int:pk>/update/', deliverycompany_update, name='deliverycompany_update'),
    path('deliverycompanies/<int:pk>/delete/', deliverycompany_delete, name='deliverycompany_delete'),

    # Basket Views
    path('baskets/', basket_list, name='basket_list'),
    path('baskets/create/', basket_create, name='basket_create'),
    path('baskets/<int:pk>/', basket_detail, name='basket_detail'),
    path('baskets/<int:pk>/update/', basket_update, name='basket_update'),
    path('baskets/<int:pk>/delete/', basket_delete, name='basket_delete'),

    # BasketItem Views
    path('basketitems/', basketitem_list, name='basketitem_list'),
    path('basketitems/create/', basketitem_create, name='basketitem_create'),
    path('basketitems/<int:pk>/', basketitem_detail, name='basketitem_detail'),
    path('basketitems/<int:pk>/update/', basketitem_update, name='basketitem_update'),
    path('basketitems/<int:pk>/delete/', basketitem_delete, name='basketitem_delete'),

    # Allergen Views
    path('allergens/', allergen_list, name='allergen_list'),
    path('allergens/create/', allergen_create, name='allergen_create'),
    path('allergens/<int:pk>/', allergen_detail, name='allergen_detail'),
    path('allergens/<int:pk>/update/', allergen_update, name='allergen_update'),
    path('allergens/<int:pk>/delete/', allergen_delete, name='allergen_delete'),
]