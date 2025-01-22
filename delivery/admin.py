from django.contrib import admin
from django.contrib.admin import TabularInline
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from delivery.models.cafe import Cafe
from delivery.models.cart import Cart
from delivery.models.courier import Courier
from delivery.models.delivery import Delivery
from delivery.models.order import Order
from delivery.models.product import Product

# Models
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'availability', 'create_date', )
    list_display_links = ('id', 'name', )
    ordering = ('-create_date', )
    list_filter = ('category', 'availability', )
    search_fields = ('name', 'description', 'category', )
    empty_value_display = 'Описание отсутствует'
    radio_fields = {'category': admin.VERTICAL}


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'barista_number', )
    list_display_links = ('id', 'address', )
    ordering = ('-barista_number', )
    search_fields = ('address', )
    readonly_fields = ('geolocation',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'sum', 'products_count', ) # 'full_name_link',
    list_display_links = ('id', )
    # autocomplete_fields = ('user', )
    search_fields = ('user__first_name', 'user__last_name', 'user__username', 'products', )
    readonly_fields = ('sum', )
    filter_horizontal = ('products', )


    # def full_name_link(self, obj):
    #     link = reverse('admin:auth_user_change', args=[obj.user.id])
    #     return format_html('<a href="{}">{}</a>', link, f'{obj.user.first_name} {obj.user.last_name}')
    # full_name_link.short_description = 'Имя пользователя'

    def products_count(self, obj):
        return obj.products_count
    products_count.short_description = 'Количество товаров'

    def get_queryset(self, request):
        queryset = Cart.objects.annotate(
            products_count=Count('products__id')
        )
        return queryset

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'courier_category', 'courier_status', )
    list_display_links = ('id', 'name', 'courier_category', 'courier_status', )
    search_fields = ('name', )
    list_filter = ('courier_category', 'courier_status', )
    radio_fields = {'courier_category': admin.VERTICAL, 'courier_status': admin.VERTICAL}


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_link', 'order_link', 'time_left_detailed', 'products_count', 'products_sum', 'courier_link', )
    list_display_links = ('id', 'full_name_link', 'order_link', 'time_left_detailed', 'courier_link')
    ordering = ('-time_left', )
    search_fields = ('user__first_name', 'user__last_name', 'user__username',)
    readonly_fields = ('time_left', 'geolocation', )
    #autocomplete_fields = ('user', 'courier', 'order', )

    def courier_link(self, obj):
        link = reverse('admin:delivery_courier_change', args=[obj.courier.id])
        return format_html('<a href="{}">{}</a>', link, obj.courier)
    courier_link.short_description = 'Курьер'

    def time_left_detailed(self, obj):
        return obj.time_left.strftime('%H:%M')
    time_left_detailed.short_description = 'Времени прошло'

    def full_name_link(self, obj):
        link = reverse('admin:auth_user_change', args=[obj.user.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.user.first_name} {obj.user.last_name}')
    full_name_link.short_description = 'Имя пользователя'

    def order_link(self, obj):
        link = reverse('admin:delivery_order_change', args=[obj.order.id])
        return format_html('<a href="{}">{}</a>', link, obj.order)
    order_link.short_description = 'Заказ по адресу'

    def products_sum(self, obj):
        return obj.order.sum
    products_sum.short_description = 'Товары на сумму'


    def products_count(self, obj):
        return obj.products_count
    products_count.short_description = 'Количество товаров'

    def get_queryset(self, request):
        queryset = Delivery.objects.annotate(products_count=Count('order__products__id'))
        return queryset


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_link', 'cafe', 'sum', 'products_count', 'delivery_status', 'address', 'waiting_time', )
    list_display_links = ('id', 'cafe', )
    ordering = ('-waiting_time', )
    search_fields = ('user__first_name', 'user__last_name', 'user__username', 'address', )
    filter_horizontal = ('products', )
    #autocomplete_fields = ('user', 'cafe', )
    radio_fields = {'delivery_status': admin.VERTICAL, 'payment_method': admin.VERTICAL}


    def full_name_link(self, obj):
        link = reverse('admin:auth_user_change', args=[obj.user.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.user.first_name} {obj.user.last_name}')
    full_name_link.short_description = 'Имя пользователя'

    def products_count(self, obj):
        return obj.products_count
    products_count.short_description = 'Количество товаров'

    def get_queryset(self, request):
        queryset = Order.objects.annotate(products_count=Count('products__id'))
        return queryset


