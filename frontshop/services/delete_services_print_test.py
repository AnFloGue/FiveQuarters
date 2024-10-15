import os
from dotenv import load_dotenv

from delete_services import (
    get_jwt_token,
    get_headers,
    delete_basket_item
)

# Load environment variables from .env
load_dotenv()

API_BASE_URL = os.getenv('API_URL_V1')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')

# Global variables to store the token and its expiration time
token = None
token_expiration = None

def test_get_jwt_token():
    token = get_jwt_token()
    print(f"JWT Token: {token}")

def test_get_headers():
    headers = get_headers()
    print(f"Headers: {headers}")

def test_delete_basket_item():
    basket_item_id = 2  # Example basket item ID
    result = delete_basket_item(basket_item_id)
    print(f"Delete Basket Item Result: {result}")

if __name__ == "__main__":
    test_get_jwt_token()
    test_get_headers()
    test_delete_basket_item()