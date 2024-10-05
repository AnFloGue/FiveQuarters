# read_services_print_test.py

from frontshop.read_services import (
    get_orderitem_list, get_orderitem_details,
    get_deliverycompany_list, get_deliverycompany_details,
    get_category_list, get_category_details,
    get_product_list, get_product_details,
    get_ingredient_list, get_ingredient_details,
    get_recipe_list, get_recipe_details,
    get_account_details, get_account_list,
    get_user_profile_details, get_user_profile_list
)

if __name__ == "__main__":
    try:
        
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
        
        # Ask for a specific account ID and print its details
        account_id = input("Enter the account ID: ")
        account_details = get_account_details(account_id)
    
        if account_details:
            print("--------------------------------------------------------")
            print(f"Account Details for Account ID {account_id}:")
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

        # Ask for a specific user profile ID and print its details
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
            print(f"No details found for User Profile ID {sample_user_profile_id}")

    except KeyboardInterrupt:
        print("\n")
        print("\nProcess interrupted by...me!!!. Exiting gracefully...cool, isn't it?")