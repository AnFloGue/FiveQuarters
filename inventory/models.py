from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Category(models.Model):
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

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products', blank=True, null=True)
    date_of_manufacture = models.DateField()
    date_of_expiry = models.DateField(null=True, blank=True)

    @property
    def product_name(self):
        return self.name

    def can_be_manufactured(self):
        return all(recipe.quantity <= recipe.ingredient.stock for recipe in self.recipes.all())

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        # Add more units as needed
    ]

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    stock = models.IntegerField()
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES)
    minimum_required_amount = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    @property
    def minimum_amount_required(self):
        return self.stock >= self.minimum_required_amount

class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recipes')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('product', 'ingredient')

    def __str__(self):
        return f"{self.product.name} Recipe - {self.ingredient.name} ({self.quantity}{self.ingredient.unit})"