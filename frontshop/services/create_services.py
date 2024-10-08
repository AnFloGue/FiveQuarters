import os
import requests
from dotenv import load_dotenv

# environment variables from .env
load_dotenv()

API_BASE_URL = os.getenv('API_URL_V1')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')

def get_jwt_token():
    url = f"{API_BASE_URL}/token/"
    response = requests.post(url, data={'username': API_USERNAME, 'password': API_PASSWORD})
    response.raise_for_status()
    token = response.json()['access']
    print(f"Generated Token: {token}")  # Print the generated token for testing
    return token

# Generate the token once and reuse it
token = get_jwt_token()
headers = {
    'Authorization': f'Bearer {token}'
}

def create_product(data):
    url = f"{API_BASE_URL}/products/create/"
    response = requests.post(url, data=data, headers=headers)
    if response.status_code != 201:
        print(f"Error: {response.status_code}")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("Response content is not in JSON format or is empty.")
        print(f"Response Headers: {response.headers}")
    response.raise_for_status()
    return response.json()

product_data = {
    "name": "test product1",
    "slug": "test-product1",
    "description": "test product description",
    "price": "3.00",
    "image": "",
    "date_of_manufacture": "2024-09-10",
    "date_of_expiry": "2024-12-23",
    "manufacturing_time": "1",
    "popularity": 9999,
    "is_product_of_the_week": False,
    "rating": 5,
    "category": 3
}

created_product = create_product(product_data)
print(created_product)

def create_ingredient(data):
    url = f"{API_BASE_URL}/ingredients/create/"
    response = requests.post(url, data=data, headers=headers)
    if response.status_code != 201:
        print(f"Error: {response.status_code}")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("Response content is not in JSON format or is empty.")
        print(f"Response Headers: {response.headers}")
    response.raise_for_status()
    return response.json()

ingredient_data = {
    "name": "test ingredient3",
    "slug": "test-ingredient3",
    "stock": 100,
    "unit": "kg",
    "required_amount": 10,
    "potential_allergens": 1
}

created_ingredient = create_ingredient(ingredient_data)
print(created_ingredient)