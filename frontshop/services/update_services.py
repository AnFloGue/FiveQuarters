# python
# frontshop/update_services.py

import requests
from django.conf import settings

API_BASE_URL = settings.API_BASE_URL_V1

def update_order(order_id, data):
    """
    Updates an existing order using the API.

    Args:
        order_id (int): The ID of the order to update.
        data (dict): The updated data for the order.

    Returns:
        dict: The updated order in JSON format.
    """
    try:
        response = requests.put(f"{API_BASE_URL}/orders/{order_id}/", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}