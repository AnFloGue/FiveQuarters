from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('products/', views.ProductListView.as_view(), name='product-list'),
    # path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    # path('categories/', views.CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    # path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    # path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
]