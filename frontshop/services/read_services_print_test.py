# read_services_print_test.py

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

# Setup Django
django.setup()
from frontshop.services.read_services import (
    # Account Services
    get_account_list,
    
    # DeliveryCompany Services
    get_deliverycompany_list,
    
    # Category Services
    get_category_list,
    get_category_details,
    
    # Product Services
    get_product_list,
    product_full_list,
    product_full_detail,
    get_recommended_products,
    get_stock_info,
    
    # Ingredient Services
    get_ingredient_list,
    
    # Order Services
    get_order_list,
    
    # Basket Services
    get_basket_list,
    get_basket_detail,
    get_basketitem_list,
    get_basketitem_detail,
    get_basketitem_list_with_id,
    
    # Allergen Services
    get_allergen_list,
    get_allergen_detail, get_product_detail,
)





if __name__ == "__main__":
    try:
        '''
        # ==============================================
        # Category Prints
        # ==============================================

        category_list = get_category_list()
        print("--------------------------------------------------------")
        # print(" Complete json file:")
        # print(category_list)
        print("Category Full List:")
        for category in category_list:
            print(f"Category ID: {category.get('id')}, Name: {category.get('name')}, "
                  f"Slug: {category.get('slug')}, Description: {category.get('description')}, "
                  f"Image: {category.get('image')}")
        print("\n")
        
        # ==============================================

        category_id = input("Enter the category ID: ")


        category_details = get_category_details(category_id)
        print(f"Category Details for ID {category_id}:")

        print(" Complete json file:")
        print(category_details)
        print("--------------------------------------------------------")
        print(f"Category ID: {category_details.get('id')}\n"
              f"Name: {category_details.get('name')}\n"
              f"Slug: {category_details.get('slug')}\n"
              f"Description: {category_details.get('description')}\n"
              f"Image: {category_details.get('image')}")
        print("\n")
        '''
        
        
        
        # ==============================================
        # Product Prints
        # ==============================================
        '''
        product_list = get_product_list()
        print("--------------------------------------------------------")
        print("Product List:")
        print(" Complete json file:")
        print(product_list)
        print("--------------------------------------------------------")
        
        
        available_products = []
        for product in product_list:
            
            print(f"Product ID: {product.get('id')}")
            print(f"Name: {product.get('name')}")
            print(f"Slug: {product.get('slug')}")
            print(f"Description: {product.get('description')}")
            print(f"Stock: {product.get('stock')}")
            print(f"Price: {product.get('price')}")
            print(f"Image: {product.get('image')}")
            print(f"Date of Manufacture: {product.get('date_of_manufacture')}")
            print(f"Date of Expiry: {product.get('date_of_expiry')}")
            print(f"Expired: {product.get('is_expired')}")
            print(f"Manufacturing Time: {product.get('manufacturing_time')}")
            print(f"Popularity: {product.get('popularity')}")
            print(f"Is Product of the Week: {product.get('is_product_of_the_week')}")
            print(f"Rating: {product.get('rating')}")
            print(f"Category: {product.get('category')}")

            print(f"Allergens: {product.get('allergens')}")
            print("\n")
        '''
        
        # ==============================================
        # Product Detail
        # ==============================================
        product_id = int(input("Enter the product ID for details: "))
        product_detail = get_product_detail(product_id)
        print("--------------------------------------------------------")
        print("Product Detail:")
        print(f"Product ID: {product_detail.get('id')}\n"
              f"Name: {product_detail.get('name')}\n"
              f"Description: {product_detail.get('description')}\n"
              f"Price: {product_detail.get('price')}\n"
              f"Stock: {product_detail.get('stock')}\n"
              f"Category: {product_detail.get('category')}")
        print("\n")
        
        # ==============================================
        # Recommended Products
        # ==============================================
        recommended_products = get_recommended_products()
        print("--------------------------------------------------------")
        print("Recommended Products:")
        for product in recommended_products:
            product_data = product.get('product', {})
            print(f"Product ID: {product_data.get('id')}\n"
                  f"Name: {product_data.get('name')}\n"
                  f"Popularity: {product_data.get('popularity')}\n"
                  f"Price: {product_data.get('price')}")
            print("\n")


        '''
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
        '''
        
        
        # ==============================================
        # Product Full Detail with Ingredients
        # ==============================================
        '''
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
        '''
    except KeyboardInterrupt:
        print("\n")
        print("\nProcess interrupted by...me!!!. Exiting gracefully...cool, isn't it?")