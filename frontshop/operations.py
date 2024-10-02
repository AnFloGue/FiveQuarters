# python
# frontshop/operations.py

def calculate_total_price(order_items):
    """
    Calculate the total price of an order based on its items.

    Args:
        order_items (list): A list of order items, each containing 'quantity' and 'price'.

    Returns:
        float: The total price of the order.
    """
    total_price = 0
    for item in order_items:
        total_price += item['quantity'] * item['price']
    return total_price

def filter_products_by_category(products, category_id):
    """
    Filter products by a specific category.

    Args:
        products (list): A list of products.
        category_id (int): The ID of the category to filter by.

    Returns:
        list: A list of products that belong to the specified category.
    """
    filtered_products = []
    for product in products:
        if product['category'] == category_id:
            filtered_products.append(product)
    return filtered_products