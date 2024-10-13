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
        print(f"Generated Token: {token}")  # Print the generated token for testing
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