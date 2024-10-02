# frontshop/services.py

import os
import django
import requests
from django.conf import settings

# ==============================
# Set the DJANGO_SETTINGS_MODULE environment variable
# ==============================

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')
django.setup()

# Use the API base URL from settings
API_BASE_URL = settings.API_BASE_URL_V1

# ==============================
# Order Views
# ==============================

def get_order_list():
    """
    Fetches the list of all orders from the API.

    Returns:
        list: A list of orders in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orders/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_order_details(order_id):
    """
    Fetches the details of a specific order from the API.

    Args:
        order_id (int): The ID of the order to fetch.

    Returns:
        dict: The details of the order in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orders/{order_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# ==============================
# OrderItem Views
# ==============================

def get_orderitem_list(order_id):
    """
    Fetches the list of all items for a specific order from the API.

    Args:
        order_id (int): The ID of the order to fetch items for.

    Returns:
        list: A list of order items in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orders/{order_id}/items/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_orderitem_details(orderitem_id):
    """
    Fetches the details of a specific order item from the API.

    Args:
        orderitem_id (int): The ID of the order item to fetch.

    Returns:
        dict: The details of the order item in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orderitems/{orderitem_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# ==============================
# Product Views
# ==============================

def get_product_list():
    """
    Fetches the list of all products from the API.

    Returns:
        list: A list of products in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/products/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_product_details(product_id):
    """
    Fetches the details of a specific product from the API.

    Args:
        product_id (int): The ID of the product to fetch.

    Returns:
        dict: The details of the product in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/products/{product_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


# ==============================
# Main block to call the functions and print the results for testing
# the data collection from the API
# ==============================

if __name__ == "__main__":
    
    # ==============================
    # Order Prints
    # ==============================
    
    '''
    order_id = input("Enter the order ID: ")
    sample_order_id = order_id
    sample_orderitem_id = order_id

    order_list = get_order_list()
    print("--------------------------------------------------------")
    print("Order List:")
    for order in order_list:
        print(f"Order ID: {order['id']}, Status: {order['status']}, Total Price: {order['total_price']}, "
              f"Customer's Note: {order['customers_note']}, Tracking Number: {order['tracking_number']}, "
              f"Posted Date: {order['posted_date']}, Received Date: {order['received_date']}, "
              f"Created At: {order['created_at']}, Updated At: {order['updated_at']}, "
              f"User: {order['user']}, Delivery Company: {order['delivery_company']}")
    print("\n")

    order_details = get_order_details(sample_order_id)
    print("--------------------------------------------------------")
    print(f"Order Details for Order ID {sample_order_id}:")
    print(f"Order ID: {order_details.get('id')}\n"
          f"Status: {order_details.get('status')}\n"
          f"Total Price: {order_details.get('total_price')}\n"
          f"Customer's Note: {order_details.get('customers_note')}\n"
          f"Tracking Number: {order_details.get('tracking_number')}\n"
          f"Posted Date: {order_details.get('posted_date')}\n"
          f"Received Date: {order_details.get('received_date')}\n"
          f"Created At: {order_details.get('created_at')}\n"
          f"Updated At: {order_details.get('updated_at')}\n"
          f"User: {order_details.get('user')}\n"
          f"Delivery Company: {order_details.get('delivery_company')}")
    print("\n")

    orderitem_list = get_orderitem_list(sample_order_id)
    print("--------------------------------------------------------")
    print(f"Order Item List for Order ID {sample_order_id}:")
    for item in orderitem_list:
        print(f"Item ID: {item['id']}, Quantity: {item['quantity']}, Rating: {item['rating']}, "
              f"Order: {item['order']}, Product: {item['product']}")
    print("\n")

    orderitem_details = get_orderitem_details(sample_orderitem_id)
    print("--------------------------------------------------------")
    print(f"Order Item Details for Order Item ID {sample_orderitem_id}:")
    print(f"Item ID: {orderitem_details.get('id')}\n"
          f"Name: {orderitem_details.get('name')}\n"
          f"Quantity: {orderitem_details.get('quantity')}\n"
          f"Price: {orderitem_details.get('price')}\n"
          f"Description: {orderitem_details.get('description')}")
    print("\n")
    '''
    
    # ==============================
    # Product Prints
    # ==============================
    sample_product_id = input("Enter the product ID: ")
    
    product_list = get_product_list()
    print("--------------------------------------------------------")
    print("Product Full List:")
    for product in product_list:
        print(f"Product ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, "
              f"Description: {product['description']}, Category: {product['category']}")
    print("\n")
    
    product_details = get_product_details(sample_product_id)
    print("--------------------------------------------------------")
    print(f"Product Details for Product ID {sample_product_id}:")
    print(f"Product ID: {product_details.get('id')}\n"
          f"Name: {product_details.get('name')}\n"
          f"Price: {product_details.get('price')}\n"
          f"Description: {product_details.get('description')}\n"
          f"Category: {product_details.get('category')}")
    print("\n")