# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, Category, Recipe, Inventory
from .serializers import ProductSerializer, CategorySerializer, RecipeSerializer, InventorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        product = self.get_object()
        rating = request.data.get('rating')
        # Add logic to handle rating
        return Response({'status': 'rating set'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        product = self.get_object()
        comment = request.data.get('comment')
        # Add logic to handle comment
        return Response({'status': 'comment added'}, status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer