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
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
    else:
        return {}

def delete_basket_item(basket_item_id):
    url = f"{API_BASE_URL}/basketitems/{basket_item_id}/delete/"
    headers = get_headers()
    response = None  # Initialize response to None

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        if response.status_code == 204:
            return "Item deleted successfully"
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error deleting basket item: {e} - {response.text if response else 'No response'}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")
        return None