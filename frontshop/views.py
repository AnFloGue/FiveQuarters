# frontshop/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .create_services import create_order
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


'''
def create_order_view(request):
    if request.method == 'POST':
        data = {
            "customer_id": request.POST.get('customer_id'),
            "product_id": request.POST.get('product_id'),
            "quantity": request.POST.get('quantity'),
            "price": request.POST.get('price'),
            "status": request.POST.get('status')
        }
        created_order = create_order(data)
        return JsonResponse(created_order)
    return render(request, 'frontshop/order_creation.html')

'''

# def order_detail(request):
#     return render(request, 'frontshop/order_detail.html')
#
# def order_item_detail(request):
#     return render(request, 'frontshop/order_item_detail.html')
#
# def order_item_list(request):
#     return render(request, 'frontshop/order_item_list.html')
#
# def order_list(request):
#     return render(request, 'frontshop/order_list.html')