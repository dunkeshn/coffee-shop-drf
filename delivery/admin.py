from django.contrib import admin

from delivery.models.cafe import Cafe
from delivery.models.cart import Cart
from delivery.models.courier import Courier
from delivery.models.delivery import Delivery
from delivery.models.order import Order
from delivery.models.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('address', 'barista_number', )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('products', )

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('products', )

