# frontshop/services/read_services.py

import os
from django.core.cache import cache

# DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

import django
django.setup()

# We use the API base URL from settings
API_BASE_URL = os.getenv('API_URL_V1')

import requests
from requests.exceptions import ConnectionError, Timeout, RequestException



# frontshop/services/read_services.py

def get_recommended_products():
    cache_key = 'recommended_products'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-list/")
        response.raise_for_status()
        products = response.json()
        # Sort products by popularity
        sorted_products = sorted(products, key=lambda x: x['product']['popularity'], reverse=True)
        cache_data(cache_key, sorted_products)
        return sorted_products
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []
    
    


def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return None

def cache_data(key, data, timeout=300):
    cache.set(key, data, timeout)

def get_cached_data(key):
    return cache.get(key)

def product_full_list():
    cache_key = 'product_full_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-list/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def product_full_detail(product_id):
    cache_key = f'product_full_detail_{product_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-detail/{product_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}
    
    

def get_account_list():
    cache_key = 'account_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    url = f"{API_BASE_URL}/accounts/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except ConnectionError:
        print("Failed to connect to the server. Please ensure the server is running.")
    except Timeout:
        print("The request timed out. Please try again later.")
    except RequestException as e:
        print(f"An error occurred: {e}")
    return []

def get_account_details(account_id):
    cache_key = f'account_details_{account_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    url = f"{API_BASE_URL}/accounts/{account_id}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except ConnectionError:
        print("Failed to connect to the server. Please ensure the server is running.")
    except Timeout:
        print("The request timed out. Please try again later.")
    except RequestException as e:
        print(f"An error occurred: {e}")
    return None

def get_user_profile_list():
    cache_key = 'user_profile_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    url = f"{API_BASE_URL}/userprofiles/"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            cache_data(cache_key, data)
            return data
        except requests.exceptions.JSONDecodeError:
            print("Error: Received invalid JSON response")
            return []
    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.text}")
        return []

def get_user_profile_details(user_profile_id):
    cache_key = f'user_profile_details_{user_profile_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    url = f"{API_BASE_URL}/userprofiles/{user_profile_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            cache_data(cache_key, data)
            return data
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

def get_order_list():
    cache_key = 'order_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/orders/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_order_details(order_id):
    cache_key = f'order_details_{order_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/orders/{order_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_orderitem_list():
    cache_key = 'orderitem_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/orderitems/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_orderitem_details(orderitem_id):
    cache_key = f'orderitem_details_{orderitem_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/orderitems/{orderitem_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_deliverycompany_list():
    cache_key = 'deliverycompany_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_deliverycompany_details(deliverycompany_id):
    cache_key = f'deliverycompany_details_{deliverycompany_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/{deliverycompany_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_category_list():
    cache_key = 'category_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/categories/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_category_details(category_id):
    cache_key = f'category_details_{category_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/categories/{category_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_product_list():
    cache_key = 'product_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/products/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_product_details(product_id):
    cache_key = f'product_details_{product_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/products/{product_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_ingredient_list():
    cache_key = 'ingredient_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_ingredient_details(ingredient_id):
    cache_key = f'ingredient_details_{ingredient_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/{ingredient_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_recipe_list():
    cache_key = 'recipe_list'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/recipes/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_recipe_details(recipe_id):
    cache_key = f'recipe_details_{recipe_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/recipes/{recipe_id}/")
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}