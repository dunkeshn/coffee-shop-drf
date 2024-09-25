from django.db import models

class Courier(models.Model):
    name = models.CharField('Имя', max_length=255)
    courier_category = models.CharField('Категория курьера', max_length=100, choices=[
        ('FOOT', 'Пеший курьер'),
        ('BICYCLE', 'Велокурьер'),
        ('CAR', 'Автокурьер'),
    ], default='CAR')
    courier_status = models.CharField('Категория курьера', max_length=100, choices=[
        ('AT_WORK', 'На работе'),
        ('RELAXING', 'Отдыхает'),
        ('BREAK', 'Перерыв'),
    ])

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'
        ordering = ('courier_status', )

    def __str__(self):
        return self.name