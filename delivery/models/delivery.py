from django.db import models

from delivery.models.courier import Courier
from delivery.models.order import Order


class Delivery(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, related_name='deliveries', verbose_name='Заказ')
    time_left = models.TimeField('Времени доставки прошло')
    geolocation = models.CharField('Геолокация (заглушка)', max_length=255)
    courier = models.ForeignKey(to=Courier, on_delete=models.PROTECT, related_name='deliveries', verbose_name='Курьер')

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ('time_left', )

    def __str__(self):
        return self.courier


