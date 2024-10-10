# frontshop/read_services.py
import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

import django
django.setup()

import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
from backshop.models import Product

# Use the API base URL from settings
API_BASE_URL = os.getenv('API_URL_V1')

def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return None
    
    



def product_full_list():
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-list/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []
    
def product_full_detail(product_id):
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-detail/{product_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}
    



# ==============================
# Account Views
# ==============================
def get_account_list():
    url = f"{API_BASE_URL}/accounts/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except ConnectionError:
        print("Failed to connect to the server. Please ensure the server is running.")
    except Timeout:
        print("The request timed out. Please try again later.")
    except RequestException as e:
        print(f"An error occurred: {e}")
    return []

def get_account_details(account_id):
    url = f"{API_BASE_URL}/accounts/{account_id}/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except ConnectionError:
        print("Failed to connect to the server. Please ensure the server is running.")
    except Timeout:
        print("The request timed out. Please try again later.")
    except RequestException as e:
        print(f"An error occurred: {e}")
    return None

# ==============================
# UserProfile Views
# ==============================

def get_user_profile_list():
    url = f"{API_BASE_URL}/userprofiles/"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error: Received invalid JSON response")
            return []
    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.text}")
        return []

def get_user_profile_details(user_profile_id):
    url = f"{API_BASE_URL}/userprofiles/{user_profile_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error: Received invalid JSON response")
            return None
    elif response.status_code == 404:
        print(f"Error: User profile with ID {user_profile_id} not found")
        return None
    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.text}")
        return None
    


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

def get_orderitem_list():
    """
    Fetches the list of all order items from the API.

    Returns:
        list: A list of order items in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orderitems/")
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
# DeliveryCompany Views
# ==============================

def get_deliverycompany_list():
    """
    Fetches the list of all delivery companies from the API.

    Returns:
        list: A list of delivery companies in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_deliverycompany_details(deliverycompany_id):
    """
    Fetches the details of a specific delivery company from the API.

    Args:
        deliverycompany_id (int): The ID of the delivery company to fetch.

    Returns:
        dict: The details of the delivery company in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/{deliverycompany_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# ==============================
# Category Views
# ==============================

def get_category_list():
    """
    Fetches the list of all categories from the API.

    Returns:
        list: A list of categories in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/categories/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_category_details(category_id):
    """
    Fetches the details of a specific category from the API.

    Args:
        category_id (int): The ID of the category to fetch.

    Returns:
        dict: The details of the category in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/categories/{category_id}/")
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
# Ingredient Views
# ==============================

def get_ingredient_list():
    """
    Fetches the list of all ingredients from the API.

    Returns:
        list: A list of ingredients in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_ingredient_details(ingredient_id):
    """
    Fetches the details of a specific ingredient from the API.

    Args:
        ingredient_id (int): The ID of the ingredient to fetch.

    Returns:
        dict: The details of the ingredient in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/{ingredient_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# ==============================
# Recipe Views
# ==============================

def get_recipe_list():
    """
    Fetches the list of all recipes from the API.

    Returns:
        list: A list of recipes in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/recipes/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_recipe_details(recipe_id):
    """
    Fetches the details of a specific recipe from the API.

    Args:
        recipe_id (int): The ID of the recipe to fetch.

    Returns:
        dict: The details of the recipe in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/recipes/{recipe_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}
