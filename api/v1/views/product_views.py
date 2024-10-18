# api/v1/views/product_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from backshop.models import Product, Category, Recipe, Ingredient, Allergen
from ..serializers import ProductSerializer, CategorySerializer, RecipeSerializer, IngredientSerializer, AllergenSerializer

# Category Views
@api_view(['GET'])
def category_list(request):
    categories = cache.get('category_list')
    if not categories:
        categories = Category.objects.all()
        cache.set('category_list', categories, timeout=60*15)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('category_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def category_detail(request, pk):
    category = cache.get(f'category_{pk}')
    if not category:
        category = get_object_or_404(Category, pk=pk)
        cache.set(f'category_{pk}', category, timeout=60*15)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['PUT'])
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'category_{pk}')
        cache.delete('category_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    cache.delete(f'category_{pk}')
    cache.delete('category_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

# Product Views
@api_view(['GET'])
def product_list(request):
    products = cache.get('product_list')
    if not products:
        products = Product.objects.all()
        cache.set('product_list', products, timeout=60*15)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('product_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def product_detail(request, pk):
    product = cache.get(f'product_{pk}')
    if not product:
        product = get_object_or_404(Product, pk=pk)
        cache.set(f'product_{pk}', product, timeout=60*15)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['PUT'])
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'product_{pk}')
        cache.delete('product_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    cache.delete(f'product_{pk}')
    cache.delete('product_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_full_list(request):
    products = Product.objects.select_related('category').prefetch_related('recipes__ingredient').all()
    product_details = []

    for product in products:
        category = product.category
        recipes = product.recipes.all()
        ingredients = [recipe.ingredient for recipe in recipes]

        allergens = set()
        for ingredient in ingredients:
            if ingredient.potential_allergens:
                allergens.add(ingredient.potential_allergens.name)

        allergen_names = list(allergens)

        product_info = {
            'product': ProductSerializer(product).data,
            'category': {
                'name': category.name,
                'slug': category.slug
            },
            'recipes': RecipeSerializer(recipes, many=True).data,
            'ingredients': IngredientSerializer(ingredients, many=True).data,
            'allergens': allergen_names
        }
        product_details.append(product_info)

    return Response(product_details, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_full_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = product.category
    recipes = product.recipes.all()
    ingredients = [recipe.ingredient for recipe in recipes]

    allergens = set()
    for ingredient in ingredients:
        if ingredient.potential_allergens:
            allergens.add(ingredient.potential_allergens.name)

    allergen_names = list(allergens)

    product_info = {
        'product': ProductSerializer(product).data,
        'category': {
            'name': category.name,
            'slug': category.slug
        },
        'recipes': RecipeSerializer(recipes, many=True).data,
        'ingredients': IngredientSerializer(ingredients, many=True).data,
        'allergens': allergen_names
    }

    return Response(product_info, status=status.HTTP_200_OK)

# Ingredient Views
@api_view(['GET'])
def ingredient_list(request):
    ingredients = cache.get('ingredient_list')
    if not ingredients:
        ingredients = Ingredient.objects.all()
        cache.set('ingredient_list', ingredients, timeout=60*15)
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ingredient_create(request):
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('ingredient_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ingredient_detail(request, pk):
    ingredient = cache.get(f'ingredient_{pk}')
    if not ingredient:
        ingredient = get_object_or_404(Ingredient, pk=pk)
        cache.set(f'ingredient_{pk}', ingredient, timeout=60*15)
    serializer = IngredientSerializer(ingredient)
    return Response(serializer.data)

@api_view(['PUT'])
def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    serializer = IngredientSerializer(ingredient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'ingredient_{pk}')
        cache.delete('ingredient_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    ingredient.delete()
    cache.delete(f'ingredient_{pk}')
    cache.delete('ingredient_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

# Recipe Views
@api_view(['GET'])
def recipe_list(request):
    recipes = cache.get('recipe_list')
    if not recipes:
        recipes = Recipe.objects.all()
        cache.set('recipe_list', recipes, timeout=60*15)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def recipe_create(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('recipe_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def recipe_detail(request, pk):
    recipe = cache.get(f'recipe_{pk}')
    if not recipe:
        recipe = get_object_or_404(Recipe, pk=pk)
        cache.set(f'recipe_{pk}', recipe, timeout=60*15)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)

@api_view(['PUT'])
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'recipe_{pk}')
        cache.delete('recipe_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    cache.delete(f'recipe_{pk}')
    cache.delete('recipe_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

# Allergen Views
@api_view(['GET'])
def allergen_list(request):
    allergens = cache.get('allergen_list')
    if not allergens:
        allergens = Allergen.objects.all()
        cache.set('allergen_list', allergens, timeout=60*15)
    serializer = AllergenSerializer(allergens, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def allergen_create(request):
    serializer = AllergenSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('allergen_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def allergen_detail(request, pk):
    allergen = cache.get(f'allergen_{pk}')
    if not allergen:
        allergen = get_object_or_404(Allergen, pk=pk)
        cache.set(f'allergen_{pk}', allergen, timeout=60*15)
    serializer = AllergenSerializer(allergen)
    return Response(serializer.data)

@api_view(['PUT'])
def allergen_update(request, pk):
    allergen = get_object_or_404(Allergen, pk=pk)
    serializer = AllergenSerializer(allergen, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'allergen_{pk}')
        cache.delete('allergen_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def allergen_delete(request, pk):
    allergen = get_object_or_404(Allergen, pk=pk)
    allergen.delete()
    cache.delete(f'allergen_{pk}')
    cache.delete('allergen_list')
    return Response(status=status.HTTP_204_NO_CONTENT)