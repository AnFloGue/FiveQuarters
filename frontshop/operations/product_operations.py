from frontshop.services.read_services import (
    get_product_list,
    get_ingredient_list,
    get_recipe_list
)

product_data = get_product_list()
ingredients = get_ingredient_list()
recipes = get_recipe_list()


def filter_products_by_allergens(product_data, allergen_id):
    """
    Filters products based on their potential allergens and prints each product.

    Args:
        product_data (list): A list of dictionaries containing product details.
        allergen_id (int): The ID of the allergen to filter by.
    """

    filtered_products = []
    for product in product_data:
        if product.get('potential_allergens', None) == allergen_id:
            filtered_products.append(product)
    # for product in filtered_products:
    #     print(f"Product ID: {product.get('id')}, Name: {product.get('name')}, Allergen: {product.get('potential_allergens')}")
    # return None
filter_products_by_allergens(product_data, 1)


filter_products_by_allergens(product_data, 1)

print(f"Filtered products:{product_data}")
for product in product_data:
    print("product", product)
    print()
    print(f"Product ID: {product.get('id')}, Name: {product.get('name')}, Allergens: {product.get('potential_allergens')}")

# def filter_products_by_allergen(products, allergen_id):
#     """
#     Filter products that don't contain a specific allergen and prints each product.
#     """
#     filtered_products = []
#     for product in products:
#         if allergen_id not in product.get('allergens', []):
#             filtered_products.append(product)
#     for product in filtered_products:
#         print(f"Product ID: {product.get('id')}, Name: {product.get('name')}, Allergens: {product.get('allergens')}")
#     return None
#
# def can_manufacture_product(product, ingredients, recipe):
#     """
#     Check if a product can be manufactured based on available ingredients and prints the result.
#     """
#     can_manufacture = True
#     for recipe_item in recipe:
#         ingredient_id = recipe_item['ingredient']
#         required_quantity = recipe_item['quantity']
#
#         ingredient = None
#         for ing in ingredients:
#             if ing['id'] == ingredient_id:
#                 ingredient = ing
#                 break
#
#         if not ingredient or ingredient['stock'] < required_quantity:
#             can_manufacture = False
#             break
#
#     print(f"Can manufacture product: {can_manufacture}")
#     return None
#
# def get_popular_products(products, limit=5):
#     """
#     Get the most popular products and prints each product.
#     """
#     sorted_products = sorted(products, key=lambda x: x['popularity'], reverse=True)
#     popular_products = []
#     for i in range(min(limit, len(sorted_products))):
#         popular_products.append(sorted_products[i])
#     for product in popular_products:
#         print(f"Product ID: {product.get('id')}, Name: {product.get('name')}, Popularity: {product.get('popularity')}")
#     return None
#
# def calculate_average_rating(products):
#     """
#     Calculate the average rating of all products and prints the result.
#     """
#     total_rating = 0
#     count = 0
#     for product in products:
#         if 'rating' in product:
#             total_rating += product['rating']
#             count += 1
#     average_rating = total_rating / count if count > 0 else 0.0
#     print(f"Average Rating: {average_rating}")
#     return None
#
# def get_products_by_category(products, category_id):
#     """
#     Get all products in a specific category and prints each product.
#     """
#     category_products = []
#     for product in products:
#         if product['category'] == category_id:
#             category_products.append(product)
#     for product in category_products:
#         print(f"Product ID: {product.get('id')}, Name: {product.get('name')}, Category: {product.get('category')}")
#     return None