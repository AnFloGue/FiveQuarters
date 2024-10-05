# read_services_print_test.py

from frontshop.read_services import (
    get_orderitem_list, get_orderitem_details,
    get_deliverycompany_list, get_deliverycompany_details,
    get_category_list, get_category_details,
    get_product_list, get_product_details,
    get_ingredient_list, get_ingredient_details,
    get_recipe_list, get_recipe_details,
    get_account_details, get_user_profile_details
)

if __name__ == "__main__":
    try:
        
        # ==============================
        # Account Prints
        # ==============================
        
        sample_account_id = input("Enter the account ID: ")
        
        account_details = get_account_details(sample_account_id)
        if account_details:
            print("--------------------------------------------------------")
            print(f"Account Details for Account ID {sample_account_id}:")
            print(f"Account ID: {account_details.get('id')}\n"
                  f"First Name: {account_details.get('first_name')}\n"
                  f"Last Name: {account_details.get('last_name')}\n"
                  f"Username: {account_details.get('username')}\n"
                  f"Email: {account_details.get('email')}\n"
                  f"Phone Number: {account_details.get('phone_number')}\n"
                  f"Date Joined: {account_details.get('date_joined')}\n"
                  f"Last Login: {account_details.get('last_login')}\n"
                  f"Is Admin: {account_details.get('is_admin')}\n"
                  f"Is Staff: {account_details.get('is_staff')}\n"
                  f"Is Active: {account_details.get('is_active')}\n"
                  f"Is Superadmin: {account_details.get('is_superadmin')}\n"
                  f"User Type: {account_details.get('user_type')}")
            print("\n")
        else:
            print(f"Failed to retrieve account details for ID {sample_account_id}")
        
        # ==============================
        # UserProfile Prints
        # ==============================
        
        sample_user_profile_id = input("Enter the user profile ID: ")
        
        user_profile_details = get_user_profile_details(sample_user_profile_id)
        if user_profile_details:
            print("--------------------------------------------------------")
            print(f"User Profile Details for User Profile ID {sample_user_profile_id}:")
            print(f"User Profile ID: {user_profile_details.get('id')}\n"
                  f"User: {user_profile_details.get('user')}\n"
                  f"Phone Number: {user_profile_details.get('phone_number')}\n"
                  f"Address Line 1: {user_profile_details.get('address_line_1')}\n"
                  f"Address Line 2: {user_profile_details.get('address_line_2')}\n"
                  f"City: {user_profile_details.get('city')}\n"
                  f"Postal Code: {user_profile_details.get('postal_code')}\n"
                  f"State: {user_profile_details.get('state')}\n"
                  f"Country: {user_profile_details.get('country')}\n"
                  f"Avatar: {user_profile_details.get('avatar')}\n"
                  f"User Type: {user_profile_details.get('user_type')}")
            print("\n")
        else:
            print(f"Failed to retrieve user profile details for ID {sample_user_profile_id}")


        '''# ==============================
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
        print("\n")'''

    except KeyboardInterrupt:
        print("\n")
        print("\nProcess interrupted by...me!!!. Exiting gracefully...cool, isn't it?")