import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_BASE_URL = os.getenv('API_URL_V1')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')
TOKEN = None

def get_token():
    global TOKEN
    if not TOKEN:
        url = f"{API_BASE_URL}/token/"
        data = {
            "username": API_USERNAME,
            "password": API_PASSWORD
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        TOKEN = response.json()['access']
    return TOKEN

def get_headers():
    return {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
    }

def create_basket_item_with_ids(data, basket_id, product_id):
    data['basket'] = basket_id
    data['product'] = product_id
    url = f"{API_BASE_URL}/basketitems/create/"
    headers = get_headers()
    print("Request URL:", url)
    print("Request Headers:", headers)
    print("Request Payload:", data)
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating basket item with IDs: {e} - {response.text if response else 'No response'}")
        if response is not None and response.status_code == 400:
            print("Response JSON:", response.json())
        return None

def get_basket_item(item_id):
    url = f"{API_BASE_URL}/basketitems/{item_id}/"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_all_basket_items():
    url = f"{API_BASE_URL}/basketitems/"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        # Test creating a basket item with IDs
        data = {
            "quantity": 10000
        }
        basket_id = 1
        product_id = 1
        created_item = create_basket_item_with_ids(data, basket_id, product_id)
        print("Created Basket Item:", created_item)

        # Get a specific basket item by ID
        item_id = 1
        basket_item = get_basket_item(item_id)
        print(f"Basket Item {item_id}: {basket_item}")

        # Get all basket items
        all_basket_items = get_all_basket_items()
        print("All Basket Items:", all_basket_items)
    except Exception as e:
        print("An error occurred:", e)