
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from inventory.models import Category, Product, Ingredient, Recipe
from .serializers import CategorySerializer, ProductSerializer, IngredientSerializer, RecipeSerializer

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        # the serializer will convert the model instances to JSON format
        serializer = CategorySerializer(categories, many=True)
        # return the JSON data to the client side
        return Response(serializer.data)
    
    # Create a new category instance with POST request we receive from the client side
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            # if the data is valid, save the data to the database
            serializer.save()
            # return the JSON data to the client side with status code 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    
    # Retrieve a single category instance with the primary key (pk) from the
    # database in order to perform the operations such as update and delete on it,
    # as an instance of the Category model
    try:
        category = Category.objects.get(pk=pk)
        
    # If the category instance with the primary key (pk) does not exist in the database,
    # it will raise a Category.DoesNotExist exception
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve a single category instance and return it in JSON format
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Update the category instance with the data received from the client side
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the updated data to the database
            serializer.save()
            return Response(serializer.data)
        # If the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Delete the category instance from the database
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        # The serializer will convert the model instances to JSON format
        serializer = ProductSerializer(products, many=True)
        # Return the JSON data to the client side
        return Response(serializer.data)
    elif request.method == 'POST':
        # Create a new product instance with POST request we receive from the client side
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the data to the database
            serializer.save()
            # Return the JSON data to the client side with status code 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    # Retrieve a single product instance with the primary key (pk) from the
    # database in order to perform the operations such as update and delete on it,
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve a single product instance and return it in JSON format
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Update the product instance with the data received from the client side
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the updated data to the database
            serializer.save()
            return Response(serializer.data)
        # If the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Delete the product instance from the database
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def ingredient_list(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        # The serializer will convert the model instances to JSON format
        serializer = IngredientSerializer(ingredients, many=True)
        # Return the JSON data to the client side
        return Response(serializer.data)
    elif request.method == 'POST':
        # Create a new ingredient instance with POST request we receive from the client side
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the data to the database
            serializer.save()
            # Return the JSON data to the client side with status code 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ingredient_detail(request, pk):
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve a single ingredient instance and return it in JSON format
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Update the ingredient instance with the data received from the client side
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the updated data to the database
            serializer.save()
            return Response(serializer.data)
        # If the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Delete the ingredient instance from the database
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        # The serializer will convert the model instances to JSON format
        serializer = RecipeSerializer(recipes, many=True)
        # Return the JSON data to the client side
        return Response(serializer.data)
    elif request.method == 'POST':
        # Create a new recipe instance with POST request we receive from the client side
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the data to the database
            serializer.save()
            # Return the JSON data to the client side with status code 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve a single recipe instance and return it in JSON format
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Update the recipe instance with the data received from the client side
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the updated data to the database
            serializer.save()
            return Response(serializer.data)
        # If the data is not valid, return the errors to the client side with status code 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Delete the recipe instance from the database
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)