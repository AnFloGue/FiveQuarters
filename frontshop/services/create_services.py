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
    print(f"Generated Token: {token}")  # Print the generated token
    return token


def create_product(data):
    token = get_jwt_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f"{API_BASE_URL}/products/create/"

    # Remove the image field if it's empty
    if 'image' in data and not data['image']:
        del data['image']

    files = {}
    if 'image' in data and data['image']:
        files = {'image': open(data['image'], 'rb')}
        # Remove image from data dict as it will be sent in files
        del data['image']

    response = requests.post(url, data=data, files=files, headers=headers)
    if response.status_code != 201:
        print(f"Error: {response.status_code}")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("Response content is not in JSON format or is empty.")
        print(f"Response Headers: {response.headers}")
        print(f"Response Text: {response.text}")
    response.raise_for_status()
    return response.json()


# Example data to be sent to the API
product_data = {
    "name": "Generated",
    "slug": "generated",
    "description": "Flaky buttery croissant",
    "price": "3.00",
    "image": "",
    "date_of_manufacture": "2024-09-10",
    "date_of_expiry": "2024-09-23",
    "manufacturing_time": "3",
    "popularity": 33241,
    "is_product_of_the_week": False,
    "rating": 5,
    "category": 3
}

created_product = create_product(product_data)
print(created_product)