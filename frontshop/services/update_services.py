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
        print(f"frontshop/services/update_services.py, Generated Token: {token}")  # Print the generated token for testing
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

def update_account(pk, data):
    response = requests.put(f'{API_BASE_URL}/accounts/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# UserProfile Services
# ==================================================

def update_user_profile(pk, data):
    response = requests.put(f'{API_BASE_URL}/user-profiles/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# Category Services
# ==================================================

def update_category(pk, data):
    response = requests.put(f'{API_BASE_URL}/categories/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# Product Services
# ==================================================

def update_product(pk, data):
    response = requests.put(f'{API_BASE_URL}/products/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# Ingredient Services
# ==================================================

def update_ingredient(pk, data):
    response = requests.put(f'{API_BASE_URL}/ingredients/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# Recipe Services
# ==================================================

def update_recipe(pk, data):
    response = requests.put(f'{API_BASE_URL}/recipes/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# Order Services
# ==================================================

def update_order(pk, data):
    response = requests.put(f'{API_BASE_URL}/orders/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# OrderItem Services
# ==================================================

def update_order_item(pk, data):
    response = requests.put(f'{API_BASE_URL}/order-items/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# DeliveryCompany Services
# ==================================================

def update_delivery_company(pk, data):
    response = requests.put(f'{API_BASE_URL}/delivery-companies/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

# ==================================================
# OrderSummary Services
# ==================================================

def update_order_summary(pk, data):
    response = requests.put(f'{API_BASE_URL}/order-summaries/{pk}/', json=data, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None

