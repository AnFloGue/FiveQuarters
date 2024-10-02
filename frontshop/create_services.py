# python
# frontshop/create_services.py

import requests
from django.conf import settings

API_BASE_URL = settings.API_BASE_URL_V1

def create_order(data):
    """
    Creates a new order using the API.

    Args:
        data (dict): The data for the new order.

    Returns:
        dict: The created order in JSON format.
    """
    try:
        response = requests.post(f"{API_BASE_URL}/orders/", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}