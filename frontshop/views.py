from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from inventory.models import Product

# List view for Orders
def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'frontshop/order_list.html', context)

# Detail view for a single Order
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order, 'items': order.items.all()}
    return render(request, 'frontshop/order_detail.html', context)

# List view for Order Items
def order_item_list(request):
    order_items = OrderItem.objects.all()
    context = {'order_items': order_items}
    return render(request, 'frontshop/order_item_list.html', context)

# Detail view for a single Order Item
def order_item_detail(request, order_item_id):
    order_item = get_object_or_404(OrderItem, id=order_item_id)
    ingredients = order_item.product.recipes.all()
    context = {
        'order_item': order_item,
        'ingredients': [recipe.ingredient for recipe in ingredients],
        'review': 'Default review',
        'stars': '*****'
    }
    return render(request, 'frontshop/order_item_detail.html', context)