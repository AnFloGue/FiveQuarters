from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at', 'updated_at')
    list_display_links = ('id', 'user')
    list_editable = ('status',)
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')
    date_hierarchy = 'created_at'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    list_display_links = ('id', 'order')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order__status',)