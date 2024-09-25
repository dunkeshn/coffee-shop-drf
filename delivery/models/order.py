from django.db import models

from delivery.models.cafe import Cafe
from delivery.models.product import Product


class Order(models.Model):
    products = models.ManyToManyField(to=Product, related_name='orders',
                                      verbose_name='Товары', null=True)
    cafe = models.ForeignKey(to=Cafe, on_delete=models.PROTECT, related_name='orders', verbose_name='Кофейни',
                             null=True)
    sum = models.FloatField('Сумма')
    delivery_status = models.CharField('Статус доставки', max_length=100, choices=[
        ('PAYING', 'Оплата заказа'),
        ('PREPARING', 'Заказ готовится'),
        ('DELIVERING', 'Заказ доставляется'),
        ('RECEIVED', 'Заказ получен'),
    ], default='PAYING')
    payment_method = models.CharField('Способ оплаты', max_length=100, choices=[
        ('BANK_CARD', 'Банковская карта'),
    ], null=True)
    address = models.TextField('Адрес')
    waiting_time = models.TimeField('Время доставки')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('waiting_time', )

    def __str__(self):
        return self.address

