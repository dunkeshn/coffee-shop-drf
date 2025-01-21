
from django.db import models

from delivery.models.courier import Courier
from delivery.models.order import Order
from users.models.users import User


class Delivery(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='deliveries', verbose_name='Пользователь',
                             null=True)
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, related_name='deliveries', verbose_name='Заказ')
    time_left = models.TimeField('Времени доставки прошло', blank=True)
    geolocation = models.CharField('Геолокация (заглушка)', max_length=255)
    courier = models.ForeignKey(to=Courier, on_delete=models.PROTECT, related_name='deliveries', verbose_name='Курьер')

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ('time_left',)

    def __str__(self):
        return f'Доставка #{self.id}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.time_left = '00:00:00'
        return super(Delivery, self).save(*args, **kwargs)
