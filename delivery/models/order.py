from django.contrib.auth.models import User
from django.db import models

from delivery.models.cafe import Cafe
from delivery.models.product import Product


class Order(models.Model):

    class DeliveryStatus(models.TextChoices):
        PAYING = 'PAYING', 'Оплата заказа'
        PREPARING = 'PREPARING', 'Заказ готовится'
        DELIVERING = 'DELIVERING', 'Заказ доставляется'
        RECEIVED = 'RECEIVED', 'Заказ получен'

    class PaymentMethod(models.TextChoices):
        BANK_CARD = 'BANK_CARD', 'Банковская карта'

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='orders', verbose_name = 'Пользователь', null=True)
    products = models.ManyToManyField(to=Product, related_name='orders',
                                      verbose_name='Товары')
    cafe = models.ForeignKey(to=Cafe, on_delete=models.PROTECT, related_name='orders', verbose_name='Кофейни',
                             null=True)
    sum = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    delivery_status = models.CharField('Статус доставки', max_length=100, choices=DeliveryStatus.choices, default=DeliveryStatus.PAYING)
    payment_method = models.CharField('Способ оплаты', max_length=100, choices=PaymentMethod.choices, null=True, default=PaymentMethod.BANK_CARD)
    address = models.TextField('Адрес')
    waiting_time = models.TimeField('Ожидаемое время доставки', blank=True, default='00:05:00')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('waiting_time', )

    def __str__(self):
        return self.address
