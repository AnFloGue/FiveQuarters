from django.shortcuts import render
from .services import get_order_list, get_order_details
from requests.exceptions import RequestException

def order_list(request):
    try:
        orders = get_order_list()
        return render(request, 'frontshop/order_list.html', {'orders': orders})
    except RequestException as e:
        return render(request, 'frontshop/order_list.html', {'error': f"Failed to fetch orders: {str(e)}"})

def order_detail(request, order_id):
    try:
        order_details = get_order_details(order_id)
        return render(request, 'frontshop/order_detail.html', {"order": order_details})
    except RequestException as e:
        return render(request, 'frontshop/order_detail.html', {"error": f"Failed to fetch order details: {str(e)}"})

def order_item_list(request):
    # Implement the logic to fetch and render the order items list
    order_items = []  # Replace with actual logic to fetch order items
    return render(request, 'frontshop/order_item_list.html', {'order_items': order_items})


def order_item_detail(request, order_item_id):
    # Implement the logic to fetch and render the order item details
    order_item_details = {}  # Replace with actual logic to fetch order item details
    return render(request, 'frontshop/order_item_detail.html', {'order_item': order_item_details})
