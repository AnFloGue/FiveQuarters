
# api/models.py
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    # Add other fields here
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    
    # Add other fields here
    
    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    # Add other fields here
    
    def __str__(self):
        return f'{self.product.name} - {self.quantity}'

