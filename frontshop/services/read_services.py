# frontshop/services/read_services.py
import os
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

# DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

# We use the API base URL from settings
API_BASE_URL = os.getenv('API_URL_V1')


#==================================================
# Functions for API requests
#==================================================

# Function to get headers for API requests
def get_headers():
    """
    Prepares the headers required for API requests, including the Authorization token.

    The function fetches the API username and password from environment variables
    and uses HTTP Basic Authentication to generate the Authorization header.

    Returns:
        dict: A dictionary containing the Authorization header.
    """
    # Retrieve the API username from environment variables
    username = os.getenv('API_USERNAME')
    # Retrieve the API password from environment variables
    password = os.getenv('API_PASSWORD')
    # Return a dictionary containing the Authorization header with HTTP Basic Authentication
    return {
        "Authorization": f"Basic {HTTPBasicAuth(username, password)}"
    }


def get_api_data(url):
    """
    Makes a GET request to a specified URL and returns the JSON response.

    Args:
        url (str): The URL to which the GET request is made.

    Returns:
        dict or None: The JSON response from the API if the request is successful,
                      otherwise None if an error occurs.

    Raises:
        RequestException: If an error occurs during the request.
    """
    try:
        # Make a GET request to the specified URL with the provided headers
        # The headers include the Authorization token for authentication and are used to authenticate the API request.
        response = requests.get(url, headers=get_headers())
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        # Return the JSON response from the API if the request is successful
        return response.json()
    except RequestException as err:
        # Print an error message if an exception occurs during the request
        print(f"Request error occurred: {err}")
        # Return None if an error occurs
        return None


#==================================================
# Category Services
#==================================================

def get_category_list():
    try:
        response = requests.get(f"{API_BASE_URL}/categories/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_category_details(category_id):
    try:
        response = requests.get(f"{API_BASE_URL}/categories/{category_id}/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


#==================================================
# Product Services
#==================================================

def get_product_list():
    try:
        response = requests.get(f"{API_BASE_URL}/products/", headers=get_headers())
        response.raise_for_status()
        products = response.json()
        for product in products:
            product['stock'] = product.get('stock', 0)
        return products
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def product_full_detail(product_id):
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-detail/{product_id}/", headers=get_headers())
        response.raise_for_status()
        product_data = response.json()
        if 'stock' not in product_data['product']:
            product_data['product']['stock'] = 0
        return product_data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


def product_full_list():
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-list/", headers=get_headers())
        response.raise_for_status()
        products = response.json()
        for product in products:
            product['product']['stock'] = product['product'].get('stock', 0)
        return products
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_recommended_products():
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-list/", headers=get_headers())
        response.raise_for_status()
        products = response.json()
        
        # Extract popularity values and sort products
        products_with_popularity = []
        for product in products:
            products_with_popularity.append((product, product['product']['popularity']))
        
        products_with_popularity.sort(key=lambda x: x[1], reverse=True)
        
        sorted_products = []
        for product, popularity in products_with_popularity:
            sorted_products.append(product)
        
        return sorted_products
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_stock_info(basketitems):
    stock_info = []
    for item in basketitems:
        product_id = item.product.id
        try:
            response = requests.get(f"{API_BASE_URL}/products/{product_id}/", headers=get_headers())
            response.raise_for_status()
            product_data = response.json()
            stock_available = product_data.get('stock', 0)
            quantity_needed = item.quantity
            to_be_manufactured = max(0, quantity_needed - stock_available)
            stock_info.append({
                'product_name': product_data.get('name'),
                'quantity_needed': quantity_needed,
                'stock_available': stock_available,
                'to_be_manufactured': to_be_manufactured,
            })
        except RequestException as err:
            print(f"Request error occurred: {err}")
            stock_info.append({
                'product_name': item.product.name,
                'quantity_needed': item.quantity,
                'stock_available': 'Error retrieving stock',
                'to_be_manufactured': 'Error retrieving stock',
            })
    return stock_info


#==================================================
# Ingredient Services
#==================================================

def get_ingredient_list():
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


#==================================================
# Account Services
#==================================================

def get_account_list():
    try:
        response = requests.get(f"{API_BASE_URL}/accounts/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


#==================================================
# DeliveryCompany Services
#==================================================

def get_deliverycompany_list():
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


#==================================================
# Order Services
#==================================================

def get_order_list():
    try:
        response = requests.get(f"{API_BASE_URL}/orders/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


#==================================================
# Basket Services
#==================================================

def get_basket_list():
    try:
        response = requests.get(f"{API_BASE_URL}/baskets/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_basket_detail(pk):
    try:
        response = requests.get(f"{API_BASE_URL}/baskets/{pk}/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


def get_basketitem_list():
    try:
        response = requests.get(f"{API_BASE_URL}/basketitems/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_basketitem_detail(pk):
    try:
        response = requests.get(f"{API_BASE_URL}/basketitems/{pk}/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


def get_basketitem_list_with_id(user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/basketitems/?user_id={user_id}", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


#==================================================
# Allergen Services
#==================================================

def get_allergen_list():
    try:
        response = requests.get(f"{API_BASE_URL}/allergens/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_allergen_detail(pk):
    try:
        response = requests.get(f"{API_BASE_URL}/allergens/{pk}/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}
