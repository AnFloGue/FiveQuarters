from django.shortcuts import render, get_object_or_404
from .models import Order
from .services import calculate_order_total, create_order, check_stock_levels, notify_inventory_admin, \
    fetch_product_of_the_week


# List all view for Orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'frontshop/order_list.html', {'orders': orders})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total = calculate_order_total(order_id)
    context = {
        'order': order,
        'total': total,
    }
    return render(request, 'frontshop/order_detail.html', context)


# List view for Order Items
def order_item_list(request):
    return render(request, 'frontshop/order_item_list.html')


# Detail view for a single Order Item
def order_item_detail(request, order_item_id):
    return render(request, 'frontshop/order_item_detail.html')
