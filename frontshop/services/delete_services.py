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

def delete_account(pk):
    response = requests.delete(f'{API_BASE_URL}/accounts/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# UserProfile Services
# ==================================================

def delete_user_profile(pk):
    response = requests.delete(f'{API_BASE_URL}/user-profiles/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# Category Services
# ==================================================

def delete_category(pk):
    response = requests.delete(f'{API_BASE_URL}/categories/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# Product Services
# ==================================================

def delete_product(pk):
    response = requests.delete(f'{API_BASE_URL}/products/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# Ingredient Services
# ==================================================

def delete_ingredient(pk):
    response = requests.delete(f'{API_BASE_URL}/ingredients/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# Recipe Services
# ==================================================

def delete_recipe(pk):
    response = requests.delete(f'{API_BASE_URL}/recipes/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# Order Services
# ==================================================

def delete_order(pk):
    response = requests.delete(f'{API_BASE_URL}/orders/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# OrderItem Services
# ==================================================

def delete_order_item(pk):
    response = requests.delete(f'{API_BASE_URL}/order-items/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# DeliveryCompany Services
# ==================================================

def delete_delivery_company(pk):
    response = requests.delete(f'{API_BASE_URL}/delivery-companies/{pk}/', headers=get_headers())
    return response.status_code == 204

# ==================================================
# OrderSummary Services
# ==================================================

def delete_order_summary(pk):
    response = requests.delete(f'{API_BASE_URL}/order-summaries/{pk}/', headers=get_headers())
    return response.status_code == 204