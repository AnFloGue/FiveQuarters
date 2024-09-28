from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from inventory.models import Category, Product, Ingredient, Recipe
from .serializers import CategorySerializer, ProductSerializer, IngredientSerializer, RecipeSerializer
from drf_yasg.utils import swagger_auto_schema

# ==============================
# Category Views
# ==============================

@api_view(['GET'])
def category_list(request):
    ''' Retrieve all categories '''
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=CategorySerializer)
@api_view(['POST'])
def category_create(request):
    ''' Create a new category '''
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def category_detail(request, pk):
    ''' Retrieve a specific category by its primary key (pk) '''
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=CategorySerializer)
@api_view(['PUT'])
def category_update(request, pk):
    ''' Update a specific category by its primary key (pk) '''
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def category_delete(request, pk):
    ''' Delete a specific category by its primary key (pk) '''
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==============================
# Product Views
# ==============================

@api_view(['GET'])
def product_list(request):
    ''' Retrieve all products '''
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=ProductSerializer)
@api_view(['POST'])
def product_create(request):
    ''' Create a new product '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def product_detail(request, pk):
    ''' Retrieve a specific product by its primary key (pk) '''
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=ProductSerializer)
@api_view(['PUT'])
def product_update(request, pk):
    ''' Update a specific product by its primary key (pk) '''
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def product_delete(request, pk):
    ''' Delete a specific product by its primary key (pk) '''
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==============================
# Ingredient Views
# ==============================

@api_view(['GET'])
def ingredient_list(request):
    ''' Retrieve all ingredients '''
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=IngredientSerializer)
@api_view(['POST'])
def ingredient_create(request):
    ''' Create a new ingredient '''
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ingredient_detail(request, pk):
    ''' Retrieve a specific ingredient by its primary key (pk) '''
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = IngredientSerializer(ingredient)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=IngredientSerializer)
@api_view(['PUT'])
def ingredient_update(request, pk):
    ''' Update a specific ingredient by its primary key (pk) '''
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = IngredientSerializer(ingredient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def ingredient_delete(request, pk):
    ''' Delete a specific ingredient by its primary key (pk) '''
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ingredient.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==============================
# Recipe Views
# ==============================

@api_view(['GET'])
def recipe_list(request):
    ''' Retrieve all recipes '''
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=RecipeSerializer)
@api_view(['POST'])
def recipe_create(request):
    ''' Create a new recipe '''
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def recipe_detail(request, pk):
    ''' Retrieve a specific recipe by its primary key (pk) '''
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=RecipeSerializer)
@api_view(['PUT'])
def recipe_update(request, pk):
    ''' Update a specific recipe by its primary key (pk) '''
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def recipe_delete(request, pk):
    ''' Delete a specific recipe by its primary key (pk) '''
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)