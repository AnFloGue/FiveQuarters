# read_services_print_product.py

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

# Setup Django
django.setup()

from frontshop.models import Basket
from frontshop.services.read_services import (
    
    # Basket Services
    get_basket_list,
    get_basket_detail,
    get_basketitem_list,
    get_basketitem_detail,
    get_basketitem_list_with_id,

)

if __name__ == "__main__":
    try:

        # ==============================================
        # Basket Prints
        # ==============================================

        # basket_list = get_basket_list()
        # print("--------------------------------------------------------")
        # print(" Complete json file:")
        #
        # print("Category Full List:")
        # for category in basket_list:
        #     print(f"Basket ID: {category.get('id')}, Name: {category.get('quantity')}, "
        #           f"Slug: {category.get('basket')}, Description: {category.get('product')}, ")
        # print("\n")

        
        # for basket in basket_list:
        #     print(f"Basket ID: {basket.get('id')}, User ID: {basket.get('user_id')}, "
        #           f"Created At: {basket.get('created_at')}, Updated At: {basket.get('updated_at')}, User: {basket.get('user')}")
        #     print("Items:")
        #     for item in basket.get('items', []):
        #         print(f"  Item ID: {item.get('id')}, Quantity: {item.get('quantity')}, "
        #               f"Basket: {item.get('basket')}, Product: {item.get('product')}")
        #     print("\n")

        # ==============================================
        # Query directly to Basket instances in the database
        # ==============================================

        # basket_id = input("Enter the category ID: ")

        baskets = Basket.objects.all()
        print("--------------------------------------------------------")
        
        print(baskets)
        print("-______________________________-")
        for basket in baskets:
            print(f"Basket ID: {basket.id}\n"
                  f"User ID: {basket.user_id}\n"
                  f"Created At: {basket.created_at}\n"
                  f"Updated At: {basket.updated_at}\nItems:")
            for item in basket.items.all():
                print(f"  Item ID: {item.id}\n  "
                      f"Quantity: {item.quantity}\n  "
                      f"Basket: {item.basket}\n  "
                      f"Product: {item.product}\n")
            print("\n")
            
            
        # print(f"Category Details for ID {basket_id}:")
        # print("--------------------------------------------------------")
        # # print(basket_details)
        # print("--------------------------------------------------------")
        # print(f"Category ID: {basket_details.get('id')}\n"
        #       f"User ID: {basket_details.get('user_id')}\n"
        #       f"Created At: {basket_details.get('created_at')}\n"
        #       f"Updated At: {basket_details.get('updated_at')}\n"
        #       f"User: {basket_details.get('user')}\n")
        # for item in basket_details.get('items', []):
        #     print(f"  Item ID: {item.get('id')}, "
        #           f"Quantity: {item.get('quantity')}, "
        #           f"Basket: {item.get('basket')}, "
        #           f"Product: {item.get('product')}")
        # print("\n")
        

        # # print(basket_details.get('items'))
        # print(basket_details.get('items')[basket_id].get('product'))
        # print("--------------------------------------------------------")
        #
        # print(" Complete json file:")
        # print(basket_details)
        # print("--------------------------------------------------------")
        # print(f"Category ID: {basket_details.get('id')}\n"
        #       f"Quantity: {basket_details.get('quantity')}\n"
        #       f"Basket: {basket_details.get('basket')}\n"
        #       f"Product: {basket_details.get('product')}\n")
        #
        # print("\n")

        
    except KeyboardInterrupt:
        print("\n")
        print("\nProcess interrupted by...me!!!. Exiting gracefully...cool, isn't it?")