# api/v1/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from backshop.models import Product, Category, Recipe, Ingredient, Allergen
from frontshop.models import Order, OrderItem, DeliveryCompany
from account.models import Account, UserProfile

from .serializers import (
    CategorySerializer, ProductSerializer, IngredientSerializer, RecipeSerializer,
    OrderSerializer, OrderItemSerializer, DeliveryCompanySerializer,
    AccountSerializer, UserProfileSerializer
)
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FiveQuarters.settings')

# ==================================================
# Authentication Views
# ==================================================

@api_view(['POST'])
def register(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# ==================================================
# Account Views
# ==================================================

@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def account_detail(request, pk):
    account = cache.get(f'account_{pk}')
    if not account:
        account = get_object_or_404(Account, pk=pk)
        cache.set(f'account_{pk}', account, timeout=60*15)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

@api_view(['GET'])
def account_list(request):
    accounts = cache.get('account_list')
    if not accounts:
        accounts = Account.objects.all()
        cache.set('account_list', accounts, timeout=60*15)
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    serializer = AccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'account_{pk}')
        cache.delete('account_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    cache.delete(f'account_{pk}')
    cache.delete('account_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

# ==================================================
# UserProfile Views
# ==================================================

@api_view(['POST'])
def create_user_profile(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile_detail(request, pk):
    user_profile = cache.get(f'user_profile_{pk}')
    if not user_profile:
        user_profile = get_object_or_404(UserProfile, pk=pk)
        cache.set(f'user_profile_{pk}', user_profile, timeout=60*15)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['GET'])
def user_profile_list(request):
    user_profiles = cache.get('user_profile_list')
    if not user_profiles:
        user_profiles = UserProfile.objects.all()
        cache.set('user_profile_list', user_profiles, timeout=60*15)
    serializer = UserProfileSerializer(user_profiles, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_user_profile(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    serializer = UserProfileSerializer(user_profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'user_profile_{pk}')
        cache.delete('user_profile_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user_profile(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    user_profile.delete()
    cache.delete(f'user_profile_{pk}')
    cache.delete('user_profile_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

# ==================================================
# Category Views
# ==================================================

@api_view(['GET'])
def category_list(request):
    categories = cache.get('category_list')
    if not categories:
        categories = Category.objects.all()
        cache.set('category_list', categories, timeout=60*15)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=CategorySerializer)
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

@swagger_auto_schema(method='put', request_body=CategorySerializer)
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

# ==================================================
# Product Views
# ==================================================

@api_view(['GET'])
def product_list(request):
    products = cache.get('product_list')
    if not products:
        products = Product.objects.all()
        cache.set('product_list', products, timeout=60*15)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=ProductSerializer)
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

@swagger_auto_schema(method='put', request_body=ProductSerializer)
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

# ==================================================
# Ingredient Views
# ==================================================

@api_view(['GET'])
def ingredient_list(request):
    ingredients = cache.get('ingredient_list')
    if not ingredients:
        ingredients = Ingredient.objects.all()
        cache.set('ingredient_list', ingredients, timeout=60*15)
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=IngredientSerializer)
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

@swagger_auto_schema(method='put', request_body=IngredientSerializer)
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

# ==================================================
# Recipe Views
# ==================================================

@api_view(['GET'])
def recipe_list(request):
    recipes = cache.get('recipe_list')
    if not recipes:
        recipes = Recipe.objects.all()
        cache.set('recipe_list', recipes, timeout=60*15)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=RecipeSerializer)
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

@swagger_auto_schema(method='put', request_body=RecipeSerializer)
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

# ==================================================
# Order Views
# ==================================================

@api_view(['GET'])
def order_list(request):
    orders = cache.get('order_list')
    if not orders:
        orders = Order.objects.all()
        cache.set('order_list', orders, timeout=60*15)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=OrderSerializer)
@api_view(['POST'])
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('order_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def order_detail(request, pk):
    order = cache.get(f'order_{pk}')
    if not order:
        order = get_object_or_404(Order, pk=pk)
        cache.set(f'order_{pk}', order, timeout=60*15)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=OrderSerializer)
@api_view(['PUT'])
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'order_{pk}')
        cache.delete('order_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    cache.delete(f'order_{pk}')
    cache.delete('order_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

# ==================================================
# OrderItem Views
# ==================================================

@api_view(['GET'])
def orderitem_list(request):
    orderitems = cache.get('orderitem_list')
    if not orderitems:
        orderitems = OrderItem.objects.all()
        cache.set('orderitem_list', orderitems, timeout=60*15)
    serializer = OrderItemSerializer(orderitems, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=OrderItemSerializer)
@api_view(['POST'])
def orderitem_create(request):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('orderitem_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def orderitem_detail(request, pk):
    orderitem = cache.get(f'orderitem_{pk}')
    if not orderitem:
        orderitem = get_object_or_404(OrderItem, pk=pk)
        cache.set(f'orderitem_{pk}', orderitem, timeout=60*15)
    serializer = OrderItemSerializer(orderitem)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=OrderItemSerializer)
@api_view(['PUT'])
def orderitem_update(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    serializer = OrderItemSerializer(orderitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'orderitem_{pk}')
        cache.delete('orderitem_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def orderitem_delete(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    orderitem.delete()
    cache.delete(f'orderitem_{pk}')
    cache.delete('orderitem_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

# ==================================================
# DeliveryCompany Views
# ==================================================

@api_view(['GET'])
def deliverycompany_list(request):
    delivery_companies = cache.get('deliverycompany_list')
    if not delivery_companies:
        delivery_companies = DeliveryCompany.objects.all()
        cache.set('deliverycompany_list', delivery_companies, timeout=60*15)
    serializer = DeliveryCompanySerializer(delivery_companies, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=DeliveryCompanySerializer)
@api_view(['POST'])
def deliverycompany_create(request):
    serializer = DeliveryCompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('deliverycompany_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deliverycompany_detail(request, pk):
    delivery_company = cache.get(f'deliverycompany_{pk}')
    if not delivery_company:
        delivery_company = get_object_or_404(DeliveryCompany, pk=pk)
        cache.set(f'deliverycompany_{pk}', delivery_company, timeout=60*15)
    serializer = DeliveryCompanySerializer(delivery_company)
    return Response

@swagger_auto_schema(method='put', request_body=DeliveryCompanySerializer)
@api_view(['PUT'])
def deliverycompany_update(request, pk):
    try:
        delivery_company = DeliveryCompany.objects.get(pk=pk)
    except DeliveryCompany.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DeliveryCompanySerializer(delivery_company, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.set(f'deliverycompany_{pk}', delivery_company, timeout=60*15)
        cache.delete('deliverycompany_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deliverycompany_delete(request, pk):
    try:
        delivery_company = DeliveryCompany.objects.get(pk=pk)
    except DeliveryCompany.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    delivery_company.delete()
    cache.delete(f'deliverycompany_{pk}')
    cache.delete('deliverycompany_list')
    return Response(status=status.HTTP_204_NO_CONTENT)