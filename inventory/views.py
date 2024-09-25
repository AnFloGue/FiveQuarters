from django.shortcuts import render
from .models import Category, Product, Ingredient, Recipe

# Your view functions here

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'inventory/home.html', context)

def inventory(request):
    ingredients = Ingredient.objects.all()
    context = {
        'ingredients': ingredients
    }
    return render(request, 'inventory.html', context)