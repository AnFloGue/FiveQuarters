from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Ingredient, Product, Recipe
# from .forms import CategoryForm, IngredientForm, ProductForm, RecipeForm



# ==============================
# Home View
# ==============================
def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'inventory/home.html', context)

# ==============================
# Category Views
# ==============================

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'inventory/category_list.html', {'categories': categories})

# def category_create(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category_list')
#     else:
#         form = CategoryForm()
#     return render(request, 'inventory/category_form.html', {'form': form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'inventory/category_detail.html', {'category': category})

# def category_update(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         form = CategoryForm(request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#             return redirect('category_detail', pk=pk)
#     else:
#         form = CategoryForm(instance=category)
#     return render(request, 'inventory/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'inventory/category_confirm_delete.html', {'category': category})

# ==============================
# Product Views
# ==============================

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'inventory/product_form.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_detail', pk=pk)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'inventory/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})

# ==============================
# Ingredient Views
# ==============================

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

# def ingredient_create(request):
#     if request.method == 'POST':
#         form = IngredientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ingredient_list')
#     else:
#         form = IngredientForm()
#     return render(request, 'inventory/ingredient_form.html', {'form': form})

def ingredient_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, 'inventory/ingredient_detail.html', {'ingredient': ingredient})

# def ingredient_update(request, pk):
#     ingredient = get_object_or_404(Ingredient, pk=pk)
#     if request.method == 'POST':
#         form = IngredientForm(request.POST, instance=ingredient)
#         if form.is_valid():
#             form.save()
#             return redirect('ingredient_detail', pk=pk)
#     else:
#         form = IngredientForm(instance=ingredient)
#     return render(request, 'inventory/ingredient_form.html', {'form': form})

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'inventory/ingredient_confirm_delete.html', {'ingredient': ingredient})

# ==============================
# Recipe Views
# ==============================

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'inventory/recipe_list.html', context)

# def recipe_create(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('recipe_list')
#     else:
#         form = RecipeForm()
#     return render(request, 'inventory/recipe_form.html', {'form': form})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'inventory/recipe_detail.html', {'recipe': recipe})

# def recipe_update(request, pk):
#     recipe = get_object_or_404(Recipe, pk=pk)
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('recipe_detail', pk=pk)
#     else:
#         form = RecipeForm(instance=recipe)
#     return render(request, 'inventory/recipe_form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'inventory/recipe_confirm_delete.html', {'recipe': recipe})