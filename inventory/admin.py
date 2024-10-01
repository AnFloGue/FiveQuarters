# admin.py
from django.contrib import admin
from .models import Category, Product, Ingredient, Recipe, Allergen


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class RecipeInline(admin.TabularInline):
    # a trick to display and use the recipe table inside the product table in the admin panel.
    model = Recipe
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'name', 'category', 'price', 'date_of_manufacture', 'date_of_expiry', 'popularity', 'is_product_of_the_week')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'date_of_manufacture', 'date_of_expiry')
    inlines = [RecipeInline]
    fields = ('name', 'slug', 'category', 'description', 'price', 'image', 'date_of_manufacture', 'date_of_expiry',
              'manufacturing_time', 'popularity', 'is_product_of_the_week')
    
    # to add new ingredients inside this table, we dont need to modify this model. it comes for free as
    # part of the Django admin's default behavior for handling foreign key. soooooo Cool!


class AllergenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stock', 'unit', 'required_amount', 'potential_allergens')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'stock', 'unit', 'required_amount', 'potential_allergens')
    list_filter = ('unit',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'ingredient', 'quantity')
    list_display_links = ('id', 'product')
    search_fields = ('product__name', 'ingredient__name')
    list_filter = ('product', 'ingredient')
