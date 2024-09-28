from django.urls import path
from . import views



urlpatterns = [
    
    # ==============================
    # Category Views
    # ==============================
    
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # ==============================
    # Product Views
    # ==============================

    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # ==============================
    # Ingredient Views
    # ==============================

    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/create/', views.ingredient_create, name='ingredient_create'),
    path('ingredients/<int:pk>/', views.ingredient_detail, name='ingredient_detail'),
    path('ingredients/<int:pk>/update/', views.ingredient_update, name='ingredient_update'),
    path('ingredients/<int:pk>/delete/', views.ingredient_delete, name='ingredient_delete'),

    # ==============================
    # Recipe Views
    # ==============================

    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/create/', views.recipe_create, name='recipe_create'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/update/', views.recipe_update, name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
]