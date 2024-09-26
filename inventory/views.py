from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Ingredient, Product, Recipe

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

# Category views

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'inventory/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'inventory/category_detail.html', {'category': category})

def add_category(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/add_category.html')

def edit_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/edit_category.html', {'category': category})

def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'inventory/delete_category.html', {'category': category})

# Ingredient views

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

def ingredient_detail(request, slug):
    ingredient = get_object_or_404(Ingredient, slug=slug)
    return render(request, 'inventory/ingredient_detail.html', {'ingredient': ingredient})

def add_ingredient(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/add_ingredient.html')

def edit_ingredient(request, slug):
    ingredient = get_object_or_404(Ingredient, slug=slug)
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/edit_ingredient.html', {'ingredient': ingredient})

def delete_ingredient(request, slug):
    ingredient = get_object_or_404(Ingredient, slug=slug)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'inventory/delete_ingredient.html', {'ingredient': ingredient})

# Product views

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'inventory/product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/add_product.html')

def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/edit_product.html', {'product': product})

def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/delete_product.html', {'product': product})

# Recipe views

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'inventory/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'inventory/recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/add_recipe.html')

def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'inventory/edit_recipe.html', {'recipe': recipe})

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'inventory/delete_recipe.html', {'recipe': recipe})