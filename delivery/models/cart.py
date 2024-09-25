from django.db import models

from delivery.models.product import Product


class Cart(models.Model):
    products = models.ManyToManyField(to=Product, related_name='carts', verbose_name='Товары',
                                      null=True)
    sum = models.FloatField('Сумма')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('products',)

    # def __str__(self):
    #     return self.adress
