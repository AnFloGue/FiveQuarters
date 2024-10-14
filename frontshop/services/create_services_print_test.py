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


# test the funcitons for
if __name__ == "__main__":
    client = APIClient(API_BASE_URL, API_USERNAME, API_PASSWORD)
    try:
        # Get a specific basket item by ID
        item_id = 1
        basket_item = client.get_basket_item(item_id)
        print(f"Basket Item {item_id}: {basket_item}")

        # Get all basket items
        all_basket_items = client.get_all_basket_items()
        print("All Basket Items:", all_basket_items)
    except Exception as e:
        print("An error occurred:", e)