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

def get_headers():
    username = os.getenv('API_USERNAME')
    password = os.getenv('API_PASSWORD')
    return {
        "Authorization": f"Basic {HTTPBasicAuth(username, password)}"
    }

def cache_data(key, data, timeout=300):
    cache.set(key, data, timeout)

def get_cached_data(key):
    return cache.get(key)

def get_api_data(url):
    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        print(f"Request error occurred: {err}")
        return None

# ==================
# Category Services
# ==================

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

# ==================
# Product Services
# ==================

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

# ==================
# Ingredient Services
# ==================

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

# ==================
# Account Services
# ==================

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

# ==================
# DeliveryCompany Services
# ==================

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

# ==================
# Order Services
# ==================

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

# ==================
# OrderSummary Services
# ==================

def get_order_summaries():
    response = requests.get(f'{API_BASE_URL}/order-summaries/')
    if response.status_code == 200:
        return response.json()
    return []

def get_order_summary_detail(pk):
    response = requests.get(f'{API_BASE_URL}/order-summaries/{pk}/')
    if response.status_code == 200:
        return response.json()
    return None

def create_order_summary(data):
    response = requests.post(f'{API_BASE_URL}/order-summaries/create/', json=data)
    if response.status_code == 201:
        return response.json()
    return None

def update_order_summary(pk, data):
    response = requests.put(f'{API_BASE_URL}/order-summaries/{pk}/update/', json=data)
    if response.status_code == 200:
        return response.json()
    return None

def delete_order_summary(pk):
    response = requests.delete(f'{API_BASE_URL}/order-summaries/{pk}/delete/')
    return response.status_code == 204