# backshop/models.py
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone


# ==============================
# Category Table
# ==============================


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True, editable=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/categories", blank=True, null=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


# ==============================
# Product Table
# ==============================


# backshop/models.py


class Product(models.Model):
    PROMOTION_CHOICES = [
        ("P_O_Week", "Product of the Week"),
        ("Christmas", "Christmas Special"),
        ("Holiday", "Holiday Special"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", unique=True, editable=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))]
    )
    image = models.ImageField(upload_to="photos/products", blank=True, null=True)
    date_of_manufacture = models.DateField()
    date_of_expiry = models.DateField(null=True, blank=True)
    manufacturing_time = models.CharField(max_length=100, blank=True, null=True)
    popularity = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    promotion_type = models.CharField(
        max_length=50, choices=PROMOTION_CHOICES, blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    rating = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    @property
    def is_expired(self):
        return self.date_of_expiry < timezone.now().date()

    @property
    def product_name(self):
        return self.name

    @classmethod
    def promotion(cls, promotion_type):
        return cls.objects.filter(promotion_type=promotion_type)


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
        ("kg", "Kilogram"),
        ("g", "Gram"),
        ("l", "Liter"),
        ("ml", "Milliliter"),
        ("pcs", "Pieces"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", unique=True, editable=True)
    stock = models.IntegerField(
        validators=[MinValueValidator(0)]
    )  # Ensure stock is never below 0
    is_active = models.BooleanField(default=True)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES)
    required_amount = models.IntegerField(
        default=10, validators=[MinValueValidator(0)]
    )  # Ensure required_amount is never below 0
    potential_allergens = models.ForeignKey(
        Allergen, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


# ==============================
# Recipe Table
# ==============================


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="recipes"
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ("product", "ingredient")

    def __str__(self):
        return f"{self.product.name} Recipe - {self.ingredient.name} ({self.quantity}{self.ingredient.unit})"
