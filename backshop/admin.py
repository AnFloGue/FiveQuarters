# admin.py
from django.contrib import admin
from .models import Category, Product, Ingredient, Recipe, Allergen


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'category', 'price', 'stock', 'date_of_expiry', 'popularity', 'is_product_of_the_week', 'rating')
    list_editable = ('category', 'stock', 'price', 'stock', 'popularity', 'is_product_of_the_week', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'date_of_manufacture', 'date_of_expiry')
    inlines = [RecipeInline]
    fields = (
        'name', 'slug', 'category', 'description', 'price', 'image', 'date_of_manufacture', 'date_of_expiry',
        'manufacturing_time', 'stock', 'popularity', 'is_product_of_the_week', 'rating'
    )


class AllergenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stock', 'unit', 'required_amount', 'potential_allergens')
    list_editable = ('stock', 'unit', 'required_amount', 'potential_allergens')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'stock', 'unit', 'required_amount', 'potential_allergens')
    list_filter = ('unit', 'potential_allergens')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id','ingredient', 'quantity')
    list_editable = ('quantity',)
    list_display_links = ('id', 'ingredient')
    search_fields = ('product__name', 'ingredient__name')
    list_filter = ('product', 'ingredient')