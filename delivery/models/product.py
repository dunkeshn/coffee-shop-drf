from django.db import models

class Product(models.Model):
    name = models.CharField('Название товара', max_length=255)
    price = models.FloatField('Цена товара')
    description = models.CharField('Описание товара', null=True, blank=True)
    category = models.CharField('Категория товара', max_length=100, choices=[
        ('DRINK', 'Напиток'),
        ('DESSERT', 'Десерт'),
        ('HOT', 'Горячее блюдо'),
    ], null=True)
    availability = models.CharField('Наличие', max_length=100, choices=[
        ('ABSENT', 'Товар отсутствует'),
        ('AVAILABLE', 'В наличии'),
    ], default='AVAILABLE')
    image = models.ImageField('Фотография товара', blank=True)
    # rating = models.FloatField('Рейтинг товара', blank=True, null=True)
    create_date = models.DateField('Дата создания товара', auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('create_date', )

    def __str__(self):
        return self.name
