import os
import django
from django.conf import settings
import requests

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

# Setup Django
django.setup()

API_BASE_URL = settings.API_BASE_URL_V1

def create_product(data):
    """
    Creates a new product using the API.

    Args:
        data (dict): The data for the new product.

    Returns:
        dict: The created product in JSON format.
    """
    try:
        response = requests.post(f"{API_BASE_URL}/products/", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# Example data to be sent to the API
product_data = {
    "name": "New Product",
    "slug": "new-product",
    "description": "Description of the new product",
    "price": "10.00",
    "image": "/media/photos/products/new_product.jpg",
    "date_of_manufacture": "2024-10-08",
    "date_of_expiry": "2025-10-08",
    "manufacturing_time": "2",
    "popularity": 0,
    "is_product_of_the_week": False,
    "rating": 0,
    "category": 1
}

created_product = create_product(product_data)
print(created_product)