import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env
load_dotenv()

API_BASE_URL = os.getenv('API_URL_V1')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')

# Global variables to store the token and its expiration time
token = None
token_expiration = None

def get_jwt_token():
    global token, token_expiration
    if token and token_expiration and datetime.now() < token_expiration:
        return token

    url = f"{API_BASE_URL}/token/"
    try:
        response = requests.post(url, data={'username': API_USERNAME, 'password': API_PASSWORD})
        response.raise_for_status()
        token = response.json()['access']
        # Assuming the token is valid for 1 hour
        token_expiration = datetime.now() + timedelta(hours=1)
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining JWT token: {e}")
        return None

def get_headers():
    token = get_jwt_token()
    if token:
        return {
            'Authorization': f'Bearer {token}'
        }
    else:
        return {}

# ==================================================
# Account Services
# ==================================================

def create_account(data):
    response = requests.post(f'{API_BASE_URL}/accounts/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# UserProfile Services
# ==================================================

def create_user_profile(data):
    response = requests.post(f'{API_BASE_URL}/user-profiles/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# Category Services
# ==================================================

def create_category(data):
    response = requests.post(f'{API_BASE_URL}/categories/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# Product Services
# ==================================================

def create_product(data):
    response = requests.post(f'{API_BASE_URL}/products/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# Ingredient Services
# ==================================================

def create_ingredient(data):
    response = requests.post(f'{API_BASE_URL}/ingredients/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# Recipe Services
# ==================================================

def create_recipe(data):
    response = requests.post(f'{API_BASE_URL}/recipes/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# Order Services
# ==================================================

def create_order(data):
    response = requests.post(f'{API_BASE_URL}/orders/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# OrderItem Services
# ==================================================

def create_order_item(data):
    response = requests.post(f'{API_BASE_URL}/order-items/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# DeliveryCompany Services
# ==================================================

def create_delivery_company(data):
    response = requests.post(f'{API_BASE_URL}/delivery-companies/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None

# ==================================================
# OrderSummary Services
# ==================================================

def create_order_summary(data):
    response = requests.post(f'{API_BASE_URL}/order-summaries/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None
# ==================================================
# Basket Services
# ==================================================

def create_basket(user_id):
    url = "http://localhost:8000/api/v1/baskets/create/"
    headers = get_headers()
    basket_data = {"user": user_id}  # Change 'user_id' to 'user'

    # Check if the basket already exists for the given user_id
    existing_basket_url = f"{API_BASE_URL}/baskets/?user_id={user_id}"
    try:
        existing_response = requests.get(existing_basket_url, headers=headers)
        existing_response.raise_for_status()
        existing_baskets = existing_response.json()
        if existing_baskets:
            for basket in existing_baskets:
                if basket['user_id'] == user_id:
                    print("Basket already exists:", basket)
                    return basket
    except requests.exceptions.RequestException as e:
        print(f"Error checking existing basket: {e} - {existing_response.text if existing_response else 'No response'}")

    # Create a new basket if it doesn't exist
    try:
        print(f"Sending POST request to {url} with data: {basket_data}")
        response = requests.post(url, json=basket_data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating basket: {e} - {response.text if response else 'No response'}")
        if response is not None and response.status_code == 400:
            print("Response JSON:", response.json())
        return None

def create_basket_item(data):
    url = "http://localhost:8000/api/v1/baskets/create/"
    headers = get_headers()
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating basket item: {e} - {response.text if response else 'No response'}")
        return None

def create_basket_item(data):
    url = f"{API_BASE_URL}/basketitems/create/"
    headers = get_headers()
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating basket item: {e} - {response.text if response else 'No response'}")
        return None
    

def create_basket_item_with_ids(id, quantity, basket_id, product, user_id):
    data = {}
    # we add to the data the basket_id and user_id
    data['id'] = id
    data['quantity'] = quantity
    data['basket'] = basket_id
    data['product'] = product
    data['user_id'] = user_id

    # we send the data to the API
    url = f"{API_BASE_URL}/basketitems/create/"
    headers = get_headers()
    # we post the data to the API
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating basket item with IDs: {e} - {response.text if response else 'No response'}")
        return None

# ==================================================
# BasketItem json data format
# ==================================================
'''{
  "id": 4,
  "quantity": 10,
  "basket": 2,
  "product": 1
},'''

# ==================================================
# Allergen Services
# ==================================================

def create_allergen(data):
    response = requests.post(f'{API_BASE_URL}/allergens/', json=data, headers=get_headers())
    if response.status_code == 201:
        return response.json()
    return None
