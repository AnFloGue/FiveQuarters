# api/v1/views/order_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from frontshop.models import Order, OrderItem, DeliveryCompany
from ..serializers import OrderSerializer, OrderItemSerializer, DeliveryCompanySerializer

@api_view(['GET'])
def order_list(request):
    orders = cache.get('order_list')
    if not orders:
        orders = list(Order.objects.all())
        cache.set('order_list', orders, timeout=60*15)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

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

@api_view(['GET'])
def orderitem_list(request):
    orderitems = cache.get('orderitem_list')
    if not orderitems:
        orderitems = OrderItem.objects.all()
        cache.set('orderitem_list', orderitems, timeout=60*15)
    serializer = OrderItemSerializer(orderitems, many=True)
    return Response(serializer.data)

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
def deliverycompany_list(request):
    delivery_companies = cache.get('deliverycompany_list')
    if not delivery_companies:
        delivery_companies = DeliveryCompany.objects.all()
        cache.set('deliverycompany_list', delivery_companies, timeout=60*15)
    serializer = DeliveryCompanySerializer(delivery_companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deliverycompany_detail(request, pk):
    delivery_company = cache.get(f'deliverycompany_{pk}')
    if not delivery_company:
        delivery_company = get_object_or_404(DeliveryCompany, pk=pk)
        cache.set(f'deliverycompany_{pk}', delivery_company, timeout=60*15)
    serializer = DeliveryCompanySerializer(delivery_company)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=DeliveryCompanySerializer)
@api_view(['PUT'])
def deliverycompany_update(request, pk):
    delivery_company = get_object_or_404(DeliveryCompany, pk=pk)
    serializer = DeliveryCompanySerializer(delivery_company, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'deliverycompany_{pk}')
        cache.delete('deliverycompany_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deliverycompany_delete(request, pk):
    delivery_company = get_object_or_404(DeliveryCompany, pk=pk)
    delivery_company.delete()
    cache.delete(f'deliverycompany_{pk}')
    cache.delete('deliverycompany_list')
    return Response(status=status.HTTP_204_NO_CONTENT)