# python
# frontshop/delete_services.py

import requests
from django.conf import settings

API_BASE_URL = settings.API_BASE_URL_V1

def delete_order(order_id):
    """
    Deletes an existing order using the API.

    Args:
        order_id (int): The ID of the order to delete.

    Returns:
        bool: True if the deletion was successful, False otherwise.
    """
    try:
        response = requests.delete(f"{API_BASE_URL}/orders/{order_id}/")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return False