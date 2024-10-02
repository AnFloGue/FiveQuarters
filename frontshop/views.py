# frontshop/views.py

from django.shortcuts import render
from .read_services import get_category_list, get_product_list, get_deliverycompany_list, get_order_list

def inventory_information(request):
    categories = get_category_list()
    products = get_product_list()
    delivery_companies = get_deliverycompany_list()
    orders = get_order_list()

    context = {
        'categories': categories,
        'products': products,
        'delivery_companies': delivery_companies,
        'orders': orders,
    }

    return render(request, 'frontshop/inventory-information.html', context)