# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, RecipeViewSet, InventoryViewSet

router_v1 = DefaultRouter()
router_v1.register(r'products', ProductViewSet)
router_v1.register(r'categories', CategoryViewSet)
router_v1.register(r'recipes', RecipeViewSet)
router_v1.register(r'inventory', InventoryViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]