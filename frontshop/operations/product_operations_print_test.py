# product_operations_print_test.py

from frontshop.operations.product_operations import (
    filter_products_by_allergens,
    filter_products_by_allergen,
    can_manufacture_product,
    get_popular_products,
    calculate_average_rating,
    get_products_by_category
)
from frontshop.services.read_services import (
    get_product_list,
    get_ingredient_list,
    get_recipe_list
)

if __name__ == "__main__":
    products = get_product_list()
    ingredients = get_ingredient_list()
    recipes = get_recipe_list()

    # Example: Filter products by potential allergen
    allergen_id = 101
    print(f"Filtered products by Potential Allergen {allergen_id}:")
    filter_products_by_allergens(products, allergen_id)
    print("\n")

    # Example: Filter products by allergen
    print(f"Filtered products by Allergen {allergen_id}:")
    filter_products_by_allergen(products, allergen_id)
    print("\n")

    # Example: Check if a product can be manufactured
    product = products[0] if products else {}
    print(f"Can manufacture product with ID {product.get('id') if product else 'N/A'}:")
    can_manufacture_product(product, ingredients, recipes)
    print("\n")

    # Example: Get popular products
    print("Popular products:")
    get_popular_products(products)
    print("\n")

    # Example: Calculate average rating
    print("Average Rating of products:")
    calculate_average_rating(products)
    print("\n")

    # Example: Get products by category
    category_id = 1
    print(f"products by Category {category_id}:")
    get_products_by_category(products, category_id)
    print("\n")