import pdb
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models

from delivery.models.product import Product


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='carts', verbose_name='Пользователь', null=True)
    products = models.ManyToManyField(to=Product, related_name='carts', verbose_name='Товары')
    sum = models.DecimalField(verbose_name='Сумма', max_digits=10, decimal_places=2, null=True, blank=True) # Сделать самоподсчет суммы

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('id', )

    def __str__(self):
        return f'Корзина #{self.id} - Сумма: {self.sum}'

    # def save(self, *args, **kwargs):
    #     super(Cart, self).save(*args, **kwargs)
    #     if self.products.all().count() == 0:
    #
    #     total = Decimal('0.00')
    #     for product in self.products.all():
    #         total += product.pricex
    #     self.sum = total
    #     return super(Cart, self).save(update_fields=['sum'])
