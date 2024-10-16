from django.contrib import admin
from .models import Order, OrderItem, DeliveryCompany, Basket, BasketItem

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
    list_display = ('id', 'order', 'product_name', 'quantity')
    list_editable = ('quantity',)
    list_display_links = ('id', 'order')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order__status',)

    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Product'

@admin.register(DeliveryCompany)
class DeliveryCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at', 'updated_at')
    list_display_links = ('id', 'user')
    search_fields = ('user__username',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'product_name', 'quantity')
    list_editable = ('quantity',)
    list_display_links = ('id', 'basket')
    search_fields = ('basket__user__username', 'product__name')
    list_filter = ('basket__created_at',)

    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Product'