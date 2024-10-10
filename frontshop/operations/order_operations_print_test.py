from frontshop.operations.order_operations import (
    calculate_total_order_cost,
    estimate_manufacturability,
    get_order_status,
    get_orders_by_date_range,
    get_top_selling_products,
    get_orders_by_status,
    get_most_ordered_products
)
from frontshop.services.read_services import (
    get_order_list,
    get_order_details,
    get_orderitem_list,
    get_product_list,
    get_product_details
)

if __name__ == "__main__":

    try:
        # ==============================
        # Test calculate_total_order_cost
        # ==============================
        order_data = get_order_details(1)  # Fetch order details for order ID 1
        result = calculate_total_order_cost(order_data)
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        print(f"Total Order Cost: {result}")
        print("\n")

        # ==============================
        # Test estimate_manufacturability
        # ==============================
        order_data = get_order_details(1)  # Fetch order details for order ID 1
        product_data = get_product_list()  # Fetch all products
        result = estimate_manufacturability(order_data, product_data)
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        print(f"Manufacturability: {result}")
        print("\n")

        # ==============================
        # Test get_order_status
        # ==============================
        order_id = 1
        result = get_order_status(order_id)
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        print(f"Order Status for ID {order_id}: {result}")
        print("\n")

        # ==============================
        # Test get_orders_by_date_range
        # ==============================
        start_date = "2024-10-01T00:00:00Z"
        end_date = "2024-10-31T23:59:59Z"
        result = get_orders_by_date_range(start_date, end_date)
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        print(f"Orders from {start_date} to {end_date}:")
        for order in result:
            for key, value in order.items():
                print(f"{key}: {value}")
            print("-----")
        print("\n")

        # ==============================
        # Test get_top_selling_products
        # ==============================
        num_products = 3
        result = get_top_selling_products(num_products)
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        print(f"Top {num_products} Selling Products:")
        for product in result:
            print("ID:", product['id'])
            print("Name:", product['name'])
            print("Slug:", product['slug'])
            print("Description:", product['description'])
            print("Price:", product['price'])
            print("Image:", product['image'])
            print("Date of Manufacture:", product['date_of_manufacture'])
            print("Date of Expiry:", product['date_of_expiry'])
            print("Manufacturing Time:", product['manufacturing_time'])
            print("Popularity:", product['popularity'])
            print("Is Product of the Week:", product['is_product_of_the_week'])
            print("Rating:", product['rating'])
            print("Category:", product['category'])
            print("Sales:", product['sales'])
            print("_________________________")
        print("\n")

        # ==============================
        # Test get_orders_by_status
        # ==============================
        orders = get_order_list()  # Fetch all orders
        status = 'pending'
        result = get_orders_by_status(orders, status)
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        print(f"Orders with status '{status}':")
        for order in result:
            for key, value in order.items():
                print(f"{key}: {value}")
            print("-----")
        print("\n")

        # ==============================
        # Test get_most_ordered_products
        # ==============================
        order_items = get_orderitem_list()  # Fetch all order items
        products = get_product_list()  # Fetch all products
        limit = 2
        result = get_most_ordered_products(order_items, products, limit)
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        print(f"Most Ordered Products:")
        for product in result:
            product_details = ", ".join([f"{key}: {value}" for key, value in product['product'].items()])
            print(f"{product_details}, Order Count: {product['order_count']}")
        print("\n")

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting gracefully...")