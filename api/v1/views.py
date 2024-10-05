# api/v1/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from backshop.models import Category, Product, Ingredient, Recipe
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
from .serializers import AccountSerializer


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
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

@api_view(['GET'])
def account_list(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_account(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_account(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    account.delete()
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
    try:
        user_profile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['GET'])
def user_profile_list(request):
    user_profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(user_profiles, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_user_profile(request, pk):
    try:
        user_profile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserProfileSerializer(user_profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user_profile(request, pk):
    try:
        user_profile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user_profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==================================================
# Category Views
# ==================================================

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=CategorySerializer)
@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=CategorySerializer)
@api_view(['PUT'])
def category_update(request, pk):
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
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==================================================
# Product Views
# ==================================================
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=ProductSerializer)
@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=ProductSerializer)
@api_view(['PUT'])
def product_update(request, pk):
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
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==================================================
# Ingredient Views
# ==================================================
@api_view(['GET'])
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=IngredientSerializer)
@api_view(['POST'])
def ingredient_create(request):
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ingredient_detail(request, pk):
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = IngredientSerializer(ingredient)
    return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=IngredientSerializer)
@api_view(['PUT'])
def ingredient_update(request, pk):
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
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=RecipeSerializer)
@api_view(['POST'])
def recipe_create(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=RecipeSerializer)
@api_view(['PUT'])
def recipe_update(request, pk):
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
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==============================
# Order Views
# ==============================





@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=OrderSerializer)
@api_view(['POST'])
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=OrderSerializer)
@api_view(['PUT'])
def order_update(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def order_delete(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==============================
# OrderItem Views
# ==============================
@api_view(['GET'])
def orderitem_list(request):
    orderitems = OrderItem.objects.all()
    serializer = OrderItemSerializer(orderitems, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=OrderItemSerializer)
@api_view(['POST'])
def orderitem_create(request):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def orderitem_detail(request, pk):
    try:
        orderitem = OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderItemSerializer(orderitem)
    return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=OrderItemSerializer)
@api_view(['PUT'])
def orderitem_update(request, pk):
    try:
        orderitem = OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderItemSerializer(orderitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def orderitem_delete(request, pk):
    try:
        orderitem = OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    orderitem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ==============================
# DeliveryCompany Views
# ==============================
@api_view(['GET'])
def deliverycompany_list(request):
    delivery_companies = DeliveryCompany.objects.all()
    serializer = DeliveryCompanySerializer(delivery_companies, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=DeliveryCompanySerializer)
@api_view(['POST'])
def deliverycompany_create(request):
    serializer = DeliveryCompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deliverycompany_detail(request, pk):
    try:
        delivery_company = DeliveryCompany.objects.get(pk=pk)
    except DeliveryCompany.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DeliveryCompanySerializer(delivery_company)
    return Response(serializer.data)


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
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deliverycompany_delete(request, pk):
    try:
        delivery_company = DeliveryCompany.objects.get(pk=pk)
    except DeliveryCompany.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    delivery_company.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)