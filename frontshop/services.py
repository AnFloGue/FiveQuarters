# frontshop/services.py

from frontshop.models import Order, OrderItem, Product
from inventory.models import Ingredient
from django.core.mail import send_mail

def calculate_order_total(order_id):
    """
    Calculate the total price for a given order.
    """
    order = Order.objects.get(id=order_id)
    total = 0
    for item in order.items.all():
        total += item.product.price * item.quantity
    return total

def create_order(customer, items):
    """
    Create a new order for a customer with the given items.
    """
    order = Order.objects.create(customer=customer) # we reate a new order object
    # based on the customer object passed in as an argument
    for item in items:
        OrderItem.objects.create(order=order, **item)
    return order

def check_stock_levels(order_id):
    """
    Check if the stock levels are sufficient to fulfill an order.
    """
    order = Order.objects.get(id=order_id)
    for item in order.orderitem_set.all():
        if item.product.stock < item.quantity:
            return False
    return True

def notify_inventory_admin(order_id):
    """
    Notify the inventory administrator if stock levels are below the minimum level.
    """
    order = Order.objects.get(id=order_id)
    for item in order.orderitem_set.all():
        if item.product.stock < item.quantity:
            send_mail(
                'Stock Alert',
                f'The stock for {item.product.name} is below the minimum level.',
                'admin@fivequarters.com',
                ['inventory_admin@fivequarters.com'],
                fail_silently=False,
            )

def fetch_product_of_the_week():
    """
    Retrieve the product of the week.
    """
    products = Product.objects.filter(is_product_of_the_week=True)
    if products.exists():
        return products.first()
    return None