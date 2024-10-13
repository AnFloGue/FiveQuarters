# read_services.py
import os
import requests
from django.core.cache import cache
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
    username = os.getenv('API_USERNAME')
    password = os.getenv('API_PASSWORD')
    return {
        "Authorization": f"Basic {HTTPBasicAuth(username, password)}"
    }

# Function to make a GET request to a specified URL and return the JSON response
def get_api_data(url):
    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return None

#==================================================
# Functions for caching
#==================================================

# Function to cache data with a specified key and timeout
def cache_data(key, data, timeout=300):
    cache.set(key, data, timeout) # Cache in milliseconds, for 5 minutes

# Function to retrieve cached data for a specified key
def get_cached_data(key):
    return cache.get(key)

#==================================================
# Category Services
#==================================================

def get_category_list():
    cache_key = 'category_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/categories/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

#==================================================
# Product Services
#==================================================

def get_product_list():
    cache_key = 'product_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/products/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_recommended_products():
    cache_key = 'recommended_products'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-list/", headers=get_headers())
        response.raise_for_status()
        products = response.json()
        sorted_products = sorted(products, key=lambda x: x['product']['popularity'], reverse=True)
        cache_data(cache_key, sorted_products)
        return sorted_products
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def product_full_list():
    cache_key = 'product_full_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-list/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def product_full_detail(product_id):
    cache_key = f'product_full_detail_{product_id}'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/product-full-detail/{product_id}/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

#==================================================
# Ingredient Services
#==================================================

def get_ingredient_list():
    cache_key = 'ingredient_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

#==================================================
# Account Services
#==================================================

def get_account_list():
    cache_key = 'account_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/accounts/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

#==================================================
# DeliveryCompany Services
#==================================================

def get_deliverycompany_list():
    cache_key = 'deliverycompany_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

#==================================================
# Order Services
#==================================================

def get_order_list():
    cache_key = 'order_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/orders/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

#==================================================
# Basket Services
#==================================================

def get_basket_list():
    cache_key = 'basket_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/baskets/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_basket_detail(pk):
    cache_key = f'basket_{pk}'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/baskets/{pk}/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_basketitem_list():
    cache_key = 'basketitem_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/basketitems/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_basketitem_detail(pk):
    cache_key = f'basketitem_{pk}'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/basketitems/{pk}/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

def get_basketitem_list(user_id):
    cache_key = f'basketitem_list_{user_id}'
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/basketitems/?user_id={user_id}", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

#==================================================
# Allergen Services
#==================================================

def get_allergen_list():
    cache_key = 'allergen_list'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/allergens/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_allergen_detail(pk):
    cache_key = f'allergen_{pk}'
    cached_data = get_cached_data(cache_key)
    if (cached_data):
        return cached_data
    try:
        response = requests.get(f"{API_BASE_URL}/allergens/{pk}/", headers=get_headers())
        response.raise_for_status()
        data = response.json()
        cache_data(cache_key, data)
        return data
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return {}