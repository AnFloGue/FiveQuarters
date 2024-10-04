# frontshop/read_services.py

import os
import django
import requests
from django.conf import settings

# ==============================
# Set the DJANGO_SETTINGS_MODULE environment variable
# ==============================

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')
django.setup()

# Use the API base URL from settings
API_BASE_URL = settings.API_BASE_URL_V1

# ==============================
# Order Views
# ==============================

def get_order_list():
    """
    Fetches the list of all orders from the API.

    Returns:
        list: A list of orders in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orders/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_order_details(order_id):
    """
    Fetches the details of a specific order from the API.

    Args:
        order_id (int): The ID of the order to fetch.

    Returns:
        dict: The details of the order in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orders/{order_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# ==============================
# OrderItem Views
# ==============================

def get_orderitem_list():
    """
    Fetches the list of all order items from the API.

    Returns:
        list: A list of order items in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orderitems/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_orderitem_details(orderitem_id):
    """
    Fetches the details of a specific order item from the API.

    Args:
        orderitem_id (int): The ID of the order item to fetch.

    Returns:
        dict: The details of the order item in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/orderitems/{orderitem_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


# ==============================
# DeliveryCompany Views
# ==============================

def get_deliverycompany_list():
    """
    Fetches the list of all delivery companies from the API.

    Returns:
        list: A list of delivery companies in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_deliverycompany_details(deliverycompany_id):
    """
    Fetches the details of a specific delivery company from the API.

    Args:
        deliverycompany_id (int): The ID of the delivery company to fetch.

    Returns:
        dict: The details of the delivery company in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/{deliverycompany_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


def get_deliverycompany_details(deliverycompany_id):
    """
    Fetches the details of a specific delivery company from the API.

    Args:
        deliverycompany_id (int): The ID of the delivery company to fetch.

    Returns:
        dict: The details of the delivery company in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/deliverycompanies/{deliverycompany_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# ==============================
# Category Views
# ==============================

def get_category_list():
    """
    Fetches the list of all categories from the API.

    Returns:
        list: A list of categories in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/categories/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_category_details(category_id):
    """
    Fetches the details of a specific category from the API.

    Args:
        category_id (int): The ID of the category to fetch.

    Returns:
        dict: The details of the category in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/categories/{category_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}
    
    # ==============================
    # Product Views
    # ==============================


def get_product_list():
    """
    Fetches the list of all products from the API.

    Returns:
        list: A list of products in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/products/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_product_details(product_id):
    """
    Fetches the details of a specific product from the API.

    Args:
        product_id (int): The ID of the product to fetch.

    Returns:
        dict: The details of the product in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/products/{product_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

# ==============================
# Ingredient Views
# ==============================

def get_ingredient_list():
    """
    Fetches the list of all ingredients from the API.

    Returns:
        list: A list of ingredients in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []

def get_ingredient_details(ingredient_id):
    """
    Fetches the details of a specific ingredient from the API.

    Args:
        ingredient_id (int): The ID of the ingredient to fetch.

    Returns:
        dict: The details of the ingredient in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/{ingredient_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


def get_ingredient_details(ingredient_id):
    """
    Fetches the details of a specific ingredient from the API.

    Args:
        ingredient_id (int): The ID of the ingredient to fetch.

    Returns:
        dict: The details of the ingredient in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients/{ingredient_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}


# ==============================
# Recipe Views
# ==============================

def get_recipe_list():
    """
    Fetches the list of all recipes from the API.

    Returns:
        list: A list of recipes in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/recipes/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return []


def get_recipe_details(recipe_id):
    """
    Fetches the details of a specific recipe from the API.

    Args:
        recipe_id (int): The ID of the recipe to fetch.

    Returns:
        dict: The details of the recipe in JSON format.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/recipes/{recipe_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {}

    


if __name__ == "__main__":
    try:
        # ==============================
        # OrderItem Prints
        # ==============================

        orderitem_list = get_orderitem_list()
        print("--------------------------------------------------------")
        print("Order Item Full List:")

        for item in orderitem_list:
            print(f"Order Item ID: {item.get('id')}, Quantity: {item.get('quantity')}, "
                  f"Rating: {item.get('rating')}, Order: {item.get('order')}, Product: {item.get('product')}")
        print("\n")
        # print(orderitem_list)

        sample_orderitem_id = input("Enter the order item ID: ")

        orderitem_details = get_orderitem_details(sample_orderitem_id)
        print("--------------------------------------------------------")
        print(f"Order Item Details for Order Item ID {sample_orderitem_id}:")
        print(f"Order Item ID: {orderitem_details.get('id')}\n"
              f"Quantity: {orderitem_details.get('quantity')}\n"
              f"Rating: {orderitem_details.get('rating')}\n"
              f"Order: {orderitem_details.get('order')}\n"
              f"Product: {orderitem_details.get('product')}")
        print("\n")

        # ==============================
        # DeliveryCompany Prints
        # ==============================

        deliverycompany_list = get_deliverycompany_list()
        print("--------------------------------------------------------")
        print("Delivery Company Full List:")
        for company in deliverycompany_list:
            print(f"Delivery Company ID: {company.get('id')}, Name: {company.get('name')}")
        print("\n")

        sample_deliverycompany_id = input("Enter the delivery company ID: ")

        deliverycompany_details = get_deliverycompany_details(sample_deliverycompany_id)
        print("--------------------------------------------------------")
        print(f"Delivery Company Details for ID {sample_deliverycompany_id}:")
        print(f"Delivery Company ID: {deliverycompany_details.get('id')}\n"
              f"Name: {deliverycompany_details.get('name')}\n")
        print("\n")

        # ==============================
        # Category Prints
        # ==============================

        category_list = get_category_list()
        print("--------------------------------------------------------")
        print("Category Full List:")
        for category in category_list:
            print(f"Category ID: {category.get('id')}, Name: {category.get('name')}, "
                  f"Slug: {category.get('slug')}, Description: {category.get('description')}, "
                  f"Image: {category.get('image')}")
        print("\n")

        sample_category_id = input("Enter the category ID: ")

        category_details = get_category_details(sample_category_id)
        print("--------------------------------------------------------")
        print(f"Category Details for ID {sample_category_id}:")
        print(f"Category ID: {category_details.get('id')}\n"
              f"Name: {category_details.get('name')}\n"
              f"Slug: {category_details.get('slug')}\n"
              f"Description: {category_details.get('description')}\n"
              f"Image: {category_details.get('image')}")
        print("\n")

        # ==============================
        # Product Prints
        # ==============================

        product_list = get_product_list()
        print("--------------------------------------------------------")
        print("Product Full List:")
        for product in product_list:
            print(f"Product ID: {product.get('id')}, Name: {product.get('name')}, "
                  f"Slug: {product.get('slug')}, Description: {product.get('description')}, "
                  f"Price: {product.get('price')}, Image: {product.get('image')}, "
                  f"Date of Manufacture: {product.get('date_of_manufacture')}, "
                  f"Date of Expiry: {product.get('date_of_expiry')}, "
                  f"Manufacturing Time: {product.get('manufacturing_time')}, "
                  f"Popularity: {product.get('popularity')}, "
                  f"Is Product of the Week: {product.get('is_product_of_the_week')}, "
                  f"Rating: {product.get('rating')}, Category: {product.get('category')}")
        print("\n")

        sample_product_id = input("Enter the product ID: ")

        product_details = get_product_details(sample_product_id)
        print("--------------------------------------------------------")
        print(f"Product Details for Product ID {sample_product_id}:")
        print(f"Product ID: {product_details.get('id')}\n"
              f"Name: {product_details.get('name')}\n"
              f"Slug: {product_details.get('slug')}\n"
              f"Description: {product_details.get('description')}\n"
              f"Price: {product_details.get('price')}\n"
              f"Image: {product_details.get('image')}\n"
              f"Date of Manufacture: {product_details.get('date_of_manufacture')}\n"
              f"Date of Expiry: {product_details.get('date_of_expiry')}\n"
              f"Manufacturing Time: {product_details.get('manufacturing_time')}\n"
              f"Popularity: {product_details.get('popularity')}\n"
              f"Is Product of the Week: {product_details.get('is_product_of_the_week')}\n"
              f"Rating: {product_details.get('rating')}\n"
              f"Category: {product_details.get('category')}")
        print("\n")

        # ==============================
        # Ingredient Prints
        # ==============================

        ingredient_list = get_ingredient_list()
        print("--------------------------------------------------------")
        print("Ingredient Full List:")
        for ingredient in ingredient_list:
            print(f"Ingredient ID: {ingredient.get('id')}, Name: {ingredient.get('name')}, "
                  f"Slug: {ingredient.get('slug')}, Stock: {ingredient.get('stock')}, "
                  f"Unit: {ingredient.get('unit')}, Required Amount: {ingredient.get('required_amount')}, "
                  f"Potential Allergens: {ingredient.get('potential_allergens')}")
        print("\n")

        sample_ingredient_id = input("Enter the ingredient ID: ")

        ingredient_details = get_ingredient_details(sample_ingredient_id)
        print("--------------------------------------------------------")
        print(f"Ingredient Details for Ingredient ID {sample_ingredient_id}:")
        print(f"Ingredient ID: {ingredient_details.get('id')}\n"
              f"Name: {ingredient_details.get('name')}\n"
              f"Slug: {ingredient_details.get('slug')}\n"
              f"Stock: {ingredient_details.get('stock')}\n"
              f"Unit: {ingredient_details.get('unit')}\n"
              f"Required Amount: {ingredient_details.get('required_amount')}\n"
              f"Potential Allergens: {ingredient_details.get('potential_allergens')}")
        print("\n")

        # ==============================
        # Recipe Prints
        # ==============================

        recipe_list = get_recipe_list()
        print("--------------------------------------------------------")
        print("Recipe Full List:")
        for recipe in recipe_list:
            print(f"Recipe ID: {recipe['id']}, Quantity: {recipe['quantity']}, Product: {recipe['product']}, Ingredient: {recipe['ingredient']}")
        print("\n")

        sample_recipe_id = input("Enter the recipe ID: ")

        recipe_details = get_recipe_details(sample_recipe_id)
        print("--------------------------------------------------------")
        print(f"Recipe Details for Recipe ID {sample_recipe_id}:")
        print(f"Recipe ID: {recipe_details.get('id')}\n"
              f"Quantity: {recipe_details.get('quantity')}\n"
              f"Product: {recipe_details.get('product')}\n"
              f"Ingredient: {recipe_details.get('ingredient')}")
        print("\n")

    except KeyboardInterrupt:
        print("\n")
        print("\nProcess interrupted by...me!!!. Exiting gracefully...cool, isn't it?")
    