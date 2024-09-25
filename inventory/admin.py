from django.contrib import admin
from .models import Category, Ingredient, Product, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_slug', 'category_description')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name', 'category_slug')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stock', 'unit', 'minimum_required_amount')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'date_of_manufacture', 'date_of_expiry')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category__category_name')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'ingredient', 'quantity')
    list_display_links = ('id', 'product')
    search_fields = ('product__name', 'ingredient__name')