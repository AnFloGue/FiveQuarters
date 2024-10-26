import json

file_path = "ProductFullList.json"
file_to_write = "ProductFullList_to_dump.json"

# Open the file using the absolute path
with open(file_path, "r") as file:
    data = json.load(file)

with open(file_to_write, "w") as data_file:
    json.dump(data, data_file)


# Print the data
print(data)

# print(data_dict)
#
# # Iterate through the list of products
# for item in data:
#     product = item["product"]
#     category = item["category"]
#     recipes = item["recipes"]
#     ingredients = item["ingredients"]
#     allergens = item["allergens"]
#
#     print(f"Product: {product['name']}")
#     print(f"  Description: {product['description']}")
#     print(f"  Price: {product['price']}")
#     print(f"  Category: {category['name']}")
#     print(f"  Allergens: {', '.join(allergens)}")
#
#     print("  Ingredients:")
#     for ingredient in ingredients:
#         print(
#             f"    - {ingredient['name']} (Stock: {ingredient['stock']}{ingredient['unit']})"
#         )
#
#     print("  Recipes:")
#     for recipe in recipes:
#         print(
#             f"    - Ingredient ID: {recipe['ingredient']}, Quantity: {recipe['quantity']}"
#         )
#
#     print()
