# frontshop/models.py

from django.db import models
from django.contrib.auth.models import User
from backshop.models import Product

# ==============================
# Delivery Company Model
# ==============================

class DeliveryCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
# ==============================
# Order Models
# ==============================

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customers_note = models.TextField(blank=True, null=True)
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    delivery_company = models.ForeignKey(DeliveryCompany, on_delete=models.SET_NULL, null=True, blank=True)
    posted_date = models.DateTimeField(blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def get_order_items(self):
        items_list = []
        for item in self.items.all():
            items_list.append(f"{item.quantity} of {item.product.name}")
        return "\n".join(items_list)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


# ==============================
# Basket Model
# ==============================

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.user.username}'s basket"

    @property
    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.total_price
        return total
    

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.basket}"

    @property
    def total_price(self):
        return self.quantity * self.product.price