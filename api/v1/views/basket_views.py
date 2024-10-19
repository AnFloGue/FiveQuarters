# api/v1/views/basket_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from frontshop.models import Basket, BasketItem
from ..serializers import BasketSerializer, BasketItemSerializer

@api_view(['GET'])
def basket_list(request):
    baskets = Basket.objects.all()
    serializer = BasketSerializer(baskets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def basket_create(request):
    serializer = BasketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def basket_detail(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    serializer = BasketSerializer(basket)
    return Response(serializer.data)

@api_view(['PUT'])
def basket_update(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    serializer = BasketSerializer(basket, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def basket_delete(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def basketitem_list(request):
    basketitems = BasketItem.objects.all()
    serializer = BasketItemSerializer(basketitems, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def basketitem_create(request):
    serializer = BasketItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def basketitem_detail(request, pk):
    basketitem = get_object_or_404(BasketItem, pk=pk)
    serializer = BasketItemSerializer(basketitem)
    return Response(serializer.data)

@api_view(['PUT'])
def basketitem_update(request, pk):
    basketitem = get_object_or_404(BasketItem, pk=pk)
    serializer = BasketItemSerializer(basketitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def basketitem_delete(request, pk):
    basketitem = get_object_or_404(BasketItem, pk=pk)
    basketitem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)