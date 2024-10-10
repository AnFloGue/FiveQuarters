# frontshop/operations/order_operations.py
from frontshop.services.read_services import (
    get_order_list,
    get_order_details,
    get_orderitem_list,
    get_product_details,
    get_ingredient_details,
    get_recipe_details
)

def calculate_total_order_cost(order_data):
    total_cost = 0
    for item in order_data.get('order_items', []):
        total_cost += item.get('quantity', 0) * item.get('price', 0)
    return total_cost

def estimate_manufacturability(order_data, product_data):
    required_ingredients = {}
    for item in order_data.get('order_items', []):
        product = None
        for p in product_data:
            if p.get('id') == item.get('product'):
                product = p
                break
        if not product:
            return False
        recipe = product.get('recipe')
        if not recipe:
            return False
        for ingredient in recipe.get('ingredients', []):
            ingredient_data = None
            for p in product_data:
                if p.get('id') == ingredient.get('ingredient'):
                    ingredient_data = p
                    break
            if not ingredient_data:
                return False
            ingredient_id = ingredient_data.get('id')
            if ingredient_id in required_ingredients:
                required_ingredients[ingredient_id] += ingredient.get('quantity', 0) * item.get('quantity', 0)
            else:
                required_ingredients[ingredient_id] = ingredient.get('quantity', 0) * item.get('quantity', 0)

    for ingredient_id, quantity in required_ingredients.items():
        ingredient = None
        for p in product_data:
            if p.get('id') == ingredient_id:
                ingredient = p
                break
        if not ingredient or ingredient.get('stock') < quantity:
            return False
    return True

def get_order_status(order_id):
    order_data = get_order_details(order_id)
    if order_data:
        return order_data.get('status', None)
    else:
        return None

def get_orders_by_date_range(start_date, end_date):
    filtered_orders = []
    all_orders = get_order_list()
    for order in all_orders:
        created_at = order.get('created_at', None)
        if created_at and start_date <= created_at <= end_date:
            filtered_orders.append(order)
    return filtered_orders

def get_top_selling_products(num_products):
    order_items = get_orderitem_list()
    product_sales = {}
    for item in order_items:
        product_id = item.get('product', None)
        if product_id:
            if product_id in product_sales:
                product_sales[product_id] += item.get('quantity', 0)
            else:
                product_sales[product_id] = item.get('quantity', 0)

    sorted_product_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    top_selling_products = []
    for i in range(min(num_products, len(sorted_product_sales))):
        product_id, sales = sorted_product_sales[i]
        product = get_product_details(product_id)
        if product:
            product['sales'] = sales
            top_selling_products.append(product)
    return top_selling_products

def get_orders_by_status(orders, status):
    filtered_orders = []
    for order in orders:
        if order['status'] == status:
            filtered_orders.append(order)
    return filtered_orders

def get_most_ordered_products(order_items, products, limit=5):
    product_counts = {}
    for item in order_items:
        product_id = item['product']
        if product_id in product_counts:
            product_counts[product_id] += item['quantity']
        else:
            product_counts[product_id] = item['quantity']

    sorted_product_counts = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)
    top_products = []
    for i in range(min(limit, len(sorted_product_counts))):
        product_id, count = sorted_product_counts[i]
        product = None
        for p in products:
            if p['id'] == product_id:
                product = p
                break
        if product:
            top_products.append({"product": product, "order_count": count})
    return top_products