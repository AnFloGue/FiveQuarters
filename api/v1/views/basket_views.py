# api/v1/views/basket_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from frontshop.models import Basket, BasketItem
from ..serializers import BasketSerializer, BasketItemSerializer

@api_view(['GET'])
def basket_list(request):
    baskets = cache.get('basket_list')
    if not baskets:
        baskets = Basket.objects.all()
        cache.set('basket_list', baskets, timeout=60*15)
    serializer = BasketSerializer(baskets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def basket_create(request):
    serializer = BasketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('basket_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def basket_detail(request, pk):
    basket = cache.get(f'basket_{pk}')
    if not basket:
        basket = get_object_or_404(Basket, pk=pk)
        cache.set(f'basket_{pk}', basket, timeout=60*15)
    serializer = BasketSerializer(basket)
    return Response(serializer.data)

@api_view(['PUT'])
def basket_update(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    serializer = BasketSerializer(basket, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'basket_{pk}')
        cache.delete('basket_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def basket_delete(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    cache.delete(f'basket_{pk}')
    cache.delete('basket_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def basketitem_list(request):
    basketitems = cache.get('basketitem_list')
    if not basketitems:
        basketitems = BasketItem.objects.all()
        cache.set('basketitem_list', basketitems, timeout=60*15)
    serializer = BasketItemSerializer(basketitems, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def basketitem_create(request):
    serializer = BasketItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete('basketitem_list')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def basketitem_detail(request, pk):
    basketitem = cache.get(f'basketitem_{pk}')
    if not basketitem:
        basketitem = get_object_or_404(BasketItem, pk=pk)
        cache.set(f'basketitem_{pk}', basketitem, timeout=60*15)
    serializer = BasketItemSerializer(basketitem)
    return Response(serializer.data)

@api_view(['PUT'])
def basketitem_update(request, pk):
    basketitem = get_object_or_404(BasketItem, pk=pk)
    serializer = BasketItemSerializer(basketitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'basketitem_{pk}')
        cache.delete('basketitem_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def basketitem_delete(request, pk):
    basketitem = get_object_or_404(BasketItem, pk=pk)
    basketitem.delete()
    cache.delete(f'basketitem_{pk}')
    cache.delete('basketitem_list')
    return Response(status=status.HTTP_204_NO_CONTENT)