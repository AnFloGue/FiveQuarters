from django.contrib import admin
from .models import Order, OrderItem, DeliveryCompany, OrderSummary


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'total_price', 'posted_date', 'created_at', 'delivery_company']
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

@admin.register(DeliveryCompany)
class DeliveryCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    
@admin.register(OrderSummary)
class OrderSummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'price_per_unit', 'total_price')
    list_display_links = ('id', 'user')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'