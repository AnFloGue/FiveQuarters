# api/v1/views/order_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from frontshop.models import Order, OrderItem, DeliveryCompany
from ..serializers import OrderSerializer, OrderItemSerializer, DeliveryCompanySerializer

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['PUT'])
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def orderitem_list(request):
    orderitems = OrderItem.objects.all()
    serializer = OrderItemSerializer(orderitems, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def orderitem_create(request):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def orderitem_detail(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    serializer = OrderItemSerializer(orderitem)
    return Response(serializer.data)

@api_view(['PUT'])
def orderitem_update(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    serializer = OrderItemSerializer(orderitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def orderitem_delete(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    orderitem.delete()
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deliverycompany_list(request):
    delivery_companies = DeliveryCompany.objects.all()
    serializer = DeliveryCompanySerializer(delivery_companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deliverycompany_detail(request, pk):
    delivery_company = get_object_or_404(DeliveryCompany, pk=pk)
    serializer = DeliveryCompanySerializer(delivery_company)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=DeliveryCompanySerializer)
@api_view(['PUT'])
def deliverycompany_update(request, pk):
    delivery_company = get_object_or_404(DeliveryCompany, pk=pk)
    serializer = DeliveryCompanySerializer(delivery_company, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deliverycompany_delete(request, pk):
    delivery_company = get_object_or_404(DeliveryCompany, pk=pk)
    delivery_company.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)