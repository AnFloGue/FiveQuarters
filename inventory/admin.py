from django.contrib import admin
from .models import Category, Product, Ingredient, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description')
    list_display_links = ('id', 'name')
    list_editable = ('slug',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'date_of_manufacture', 'date_of_expiry')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'date_of_manufacture', 'date_of_expiry')
    inlines = [RecipeInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'stock', 'unit', 'minimum_required_amount')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'stock', 'unit', 'minimum_required_amount')
    list_filter = ('unit',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'ingredient', 'quantity')
    list_display_links = ('id', 'product')
    search_fields = ('product__name', 'ingredient__name')
    list_filter = ('product', 'ingredient')