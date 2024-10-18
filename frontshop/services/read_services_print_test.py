# read_services_print_test.py

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

# Setup Django
django.setup()
from api.v1.views import product_full_list, product_full_detail
from frontshop.services.read_services import (
    get_deliverycompany_list,
    get_category_list,
    get_product_list,
    get_ingredient_list,
    product_full_list,
    product_full_detail,
)


if __name__ == "__main__":
    try:
        
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
        '''
        # ==============================
        # Product Prints
        # ==============================

        product_list = get_product_list()
        print("--------------------------------------------------------")
        print("Product Full List:")
        
        available_products = []
        for product in product_list:
            if product.get('is_available'):
                available_products.append(product)
            print(f"Product ID: {product.get('id')}, Name: {product.get('name')}, "
                  f"Slug: {product.get('slug')}, Description: {product.get('description')}, "
                  f'stock: {product.get("stock")}, '
                  
                  f"Price: {product.get('price')}, Image: {product.get('image')}, "
                  f"Date of Manufacture: {product.get('date_of_manufacture')}, "
                  f"Date of Expiry: {product.get('date_of_expiry')}, "
                  f"Manufacturing Time: {product.get('manufacturing_time')}, "
                  f"Popularity: {product.get('popularity')}, "
                  f"Is Product of the Week: {product.get('is_product_of_the_week')}, "
                  f"Rating: {product.get('rating')}, Category: {product.get('category')}, "
                  f"Is Available: {product.get('is_available')}")
            print("\n")
        
        print("Available Products:")



        
        products_with_ingredients = product_full_list()
        print("--------------------------------------------------------")
        print("Product Full List with Ingredients:")
        for product in products_with_ingredients:
            product_data = product.get('product', {})
            ingredients = product.get('ingredients', [])
            allergens = product.get('allergens', [])
            
            ingredients_list = ', '.join([ingredient['name'] for ingredient in ingredients]) if ingredients else "None"
            allergens_list = ', '.join(allergens) if allergens else "None"
            
            print(f"Product ID: {product_data.get('id')}\n"
                  f"Name: {product_data.get('name')}\n"
                  f"Description: {product_data.get('description')}\n"
                  f"Price: {product_data.get('price')}\n"
                  f"Ingredients: {ingredients_list}\n"
                  f"Allergens: {allergens_list}")
            print("\n")
        
        # ==============================
        # Product Full Detail with Ingredients
        # ==============================
        product_id = int(input("Enter the product ID: "))
        product_details = product_full_detail(product_id)
        print("--------------------------------------------------------")
        print("Product Full Detail with Ingredients:")
        product_data = product_details.get('product', {})
        ingredients = product_details.get('ingredients', [])
        allergens = product_details.get('allergens', [])
        
        ingredients_list = ', '.join([ingredient['name'] for ingredient in ingredients]) if ingredients else "None"
        allergens_list = ', '.join(allergens) if allergens else "None"
        
        print(f"Product ID: {product_data.get('id')}\n"
              f"Name: {product_data.get('name')}\n"
              f"Description: {product_data.get('description')}\n"
              f"Price: {product_data.get('price')}\n"
              f"Ingredients: {ingredients_list}\n"
              f"Allergens: {allergens_list}")
        print("\n")
        
    except KeyboardInterrupt:
        print("\n")
        print("\nProcess interrupted by...me!!!. Exiting gracefully...cool, isn't it?")