# api/v1/serializers.py

from rest_framework import serializers
from backshop.models import Category, Product, Ingredient, Recipe
from frontshop.models import Order, OrderItem, DeliveryCompany
from account.models import Account, UserProfile


# ================================================
# Serializers for account models
# ================================================
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# ================================================
# Serializers for backshop models
# ================================================

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_is_available(self, obj):
        return obj.is_available
    
    
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


# ================================================
# Serializers for Frontshop models
# ================================================

class DeliveryCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCompany
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'