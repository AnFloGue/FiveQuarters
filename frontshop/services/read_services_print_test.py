# read_services_print_test.py

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

# Setup Django
django.setup()
from api.v1.views import product_full_list, product_full_detail
from frontshop.services.read_services import (
    get_orderitem_list, get_orderitem_details,
    get_deliverycompany_list, get_deliverycompany_details,
    get_category_list, get_category_details,
    get_product_list, get_product_details,
    get_ingredient_list, get_ingredient_details,
    get_recipe_list, get_recipe_details,
    get_account_details, get_account_list,
    get_user_profile_details, get_user_profile_list,
    product_full_list,
    product_full_detail,
)


if __name__ == "__main__":
    try:
        '''
        # ==============================
        # Account Prints
        # ==============================

        # Fetch and print the full list of accounts
        account_list = get_account_list()
        print("--------------------------------------------------------")
        print("Account Full List:")
        for account_details in account_list:
            print(f"Account Details for Account ID {account_details.get('id')}:")
            print(f"Account ID: {account_details.get('id')}\n"
                  f"Name: {account_details.get('name')}\n"
                  f"Email: {account_details.get('email')}\n"
                  f"Date Joined: {account_details.get('date_joined')}\n"
                  f"Last Login: {account_details.get('last_login')}")
            print("\n")

        # Ask for a specific account ID and print its details
        account_id = input("Enter the account ID: ")
        account_details = get_account_details(account_id)

        if account_details:
            print("--------------------------------------------------------")
            print(f"Account Details for Account ID {account_id}:")
            print(f"Account ID: {account_details.get('id')}\n"
                  f"Name: {account_details.get('name')}\n"
                  f"Email: {account_details.get('email')}\n"
                  f"Date Joined: {account_details.get('date_joined')}\n"
                  f"Last Login: {account_details.get('last_login')}")
            print("\n")
        else:
            print(f"Failed to retrieve account details for ID {account_id}")

        # ==============================
        # UserProfile Prints
        # ==============================

        # Fetch and print the full list of user profiles
        user_profile_list = get_user_profile_list()
        print("--------------------------------------------------------")
        print("User Profile Full List:")
        for user_profile_details in user_profile_list:
            print(f"User Profile Details for User Profile ID {user_profile_details.get('id')}:")
            print(f"User Profile ID: {user_profile_details.get('id')}\n"
                  f"User: {user_profile_details.get('user')}\n"
                  f"Bio: {user_profile_details.get('bio')}\n"
                  f"Location: {user_profile_details.get('location')}\n"
                  f"Birth Date: {user_profile_details.get('birth_date')}")
            print("\n")

        # Ask for a specific user profile ID and print its details
        sample_user_profile_id = input("Enter the user profile ID: ")
        user_profile_details = get_user_profile_details(sample_user_profile_id)

        if user_profile_details:
            print("--------------------------------------------------------")
            print(f"User Profile Details for User Profile ID {sample_user_profile_id}:")
            print(f"User Profile ID: {user_profile_details.get('id')}\n"
                  f"User: {user_profile_details.get('user')}\n"
                  f"Bio: {user_profile_details.get('bio')}\n"
                  f"Location: {user_profile_details.get('location')}\n"
                  f"Birth Date: {user_profile_details.get('birth_date')}")
            print("\n")
        else:
            print(f"No details found for User Profile ID {sample_user_profile_id}")

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
        print("\n")'''

        # ==============================
        # Product Full List with Ingredients
        # ==============================
        products_with_ingredients = product_full_list()
        print("--------------------------------------------------------")
        print("Product Full List with Ingredients:")
        for product in products_with_ingredients:
            product_data = product.get('product', {})
            ingredients = product.get('ingredients', [])
            allergens = product.get('allergens', [])
            
            print(f"Product ID: {product_data.get('id')}\n"
                  f"Name: {product_data.get('name')}\n"
                  f"Description: {product_data.get('description')}\n"
                  f"Price: {product_data.get('price')}\n"
                  f"Ingredients: {', '.join([ingredient['name'] for ingredient in ingredients])}\n"
                  f"Allergens: {', '.join(allergens)}")
            print("\n")
            
        # ==============================
        # Product Full Detail with Ingredients
        # ==============================
        product_id = input("Enter the product ID: ")
        # product_id = int(input("Enter the product ID: "))
        product_details = product_full_detail(product_id)
        print("--------------------------------------------------------")
        print("Product Full Detail with Ingredients:")
        product_data = product_details.get('product', {})
        ingredients = product_details.get('ingredients', [])
        allergens = product_details.get('allergens', [])
        
        print(f"Product ID: {product_data.get('id')}\n"
              f"Name: {product_data.get('name')}\n"
              f"Description: {product_data.get('description')}\n"
              f"Price: {product_data.get('price')}\n"
              f"Ingredients: {', '.join([ingredient['name'] for ingredient in ingredients])}\n"
              f"Allergens: {', '.join(allergens)}")
        print("\n")


    except KeyboardInterrupt:
        print("\n")
        print("\nProcess interrupted by...me!!!. Exiting gracefully...cool, isn't it?")