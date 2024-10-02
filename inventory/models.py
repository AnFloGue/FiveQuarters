# inventory/models.py

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


# ==============================
# Category Table
# ==============================

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/categories', blank=True, null=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    def __str__(self):
        return self.name


# ==============================
# Product Table
# ==============================


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)  # Make slug editable
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    image = models.ImageField(upload_to='photos/products', blank=True, null=True)
    date_of_manufacture = models.DateField()
    date_of_expiry = models.DateField(null=True, blank=True)
    manufacturing_time = models.CharField(max_length=100, blank=True, null=True)
    popularity = models.PositiveIntegerField(default=0)
    is_product_of_the_week = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])


    @property
    def product_name(self):
        return self.name

    def can_be_manufactured(self):
        return all(recipe.quantity <= recipe.ingredient.stock for recipe in self.recipes.all())

    @property
    def ingredients(self):
        return [recipe.ingredient.name for recipe in self.recipes.all()]

    def __str__(self):
        return self.name

# ==============================
# Allergen Table
# ==============================

class Allergen(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

# ==============================
# Ingredient Table
# ==============================

class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        
        ('pcs', 'Pieces'),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    stock = models.IntegerField()
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES)
    required_amount = models.IntegerField(default=10)
    potential_allergens = models.ForeignKey(Allergen, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name


# ==============================
# Recipe Table
# ==============================

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recipes')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('product', 'ingredient')
    
    def __str__(self):
        return f"{self.product.name} Recipe - {self.ingredient.name} ({self.quantity}{self.ingredient.unit})"
