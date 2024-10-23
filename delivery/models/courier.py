from django.db import models

class Courier(models.Model):

    class CourierCategory(models.TextChoices):
        FOOT = 'FOOT', 'Пеший курьер'
        BICYCLE = 'BICYCLE', 'Велокурьер'
        CAR = 'CAR', 'Автокурьер'

    class CourierStatus(models.TextChoices):
        AT_WORK = 'AT_WORK', 'На работе'
        RELAXING = 'RELAXING', 'Отдыхает'
        BREAK = 'BREAK', 'Перерыв'

    name = models.CharField('Имя', max_length=255)
    courier_category = models.CharField('Категория курьера', max_length=100, choices=CourierCategory.choices,
        default=CourierCategory.CAR)
    courier_status = models.CharField('Категория курьера', max_length=100, choices=CourierStatus.choices)

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'
        ordering = ('courier_status', )

    def __str__(self):
        return f'{self.name} ({self.get_courier_category_display()})'