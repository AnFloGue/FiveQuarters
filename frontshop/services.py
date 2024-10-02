import requests
from django.conf import settings

API_BASE_URL = settings.API_BASE_URL_V1

def get_order_list():
    response = requests.get(f"{API_BASE_URL}/orders/")
    response.raise_for_status()
    return response.json()

def get_order_details(order_id):
    response = requests.get(f"{API_BASE_URL}/orders/{order_id}/")
    response.raise_for_status()
    return response.json()