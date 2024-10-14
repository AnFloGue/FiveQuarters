import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_BASE_URL = os.getenv('API_URL_V1')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')

class APIClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = None

    def get_headers(self):
        if not self.token:
            self.token = self.get_token()
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_token(self):
        url = f"{self.base_url}/token/"
        data = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()['access']

    def get_basket_item(self, item_id):
        url = f"{self.base_url}/basketitems/{item_id}/"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_all_basket_items(self):
        url = f"{self.base_url}/basketitems/"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def create_basket_item_with_ids(self, data, basket_id, product_id):
        data['basket'] = basket_id
        data['product'] = product_id
        url = f"{self.base_url}/basketitems/create/"
        headers = self.get_headers()
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

if __name__ == "__main__":
    client = APIClient(API_BASE_URL, API_USERNAME, API_PASSWORD)
    try:
        # Test creating a basket item with IDs
        data = {
            "quantity": 2
        }
        basket_id = 1
        product_id = 1
        created_item = client.create_basket_item_with_ids(data, basket_id, product_id)
        print("Created Basket Item:", created_item)

        # Get a specific basket item by ID
        item_id = 1
        basket_item = client.get_basket_item(item_id)
        print(f"Basket Item {item_id}: {basket_item}")

        # Get all basket items
        all_basket_items = client.get_all_basket_items()
        print("All Basket Items:", all_basket_items)
    except Exception as e:
        print("An error occurred:", e)