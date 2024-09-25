from django.db import models

class Cafe(models.Model):
    geolocation = models.CharField('Геолокация (заглушка)', max_length=255)
    address = models.TextField('Адрес кофейни')
    barista_number = models.IntegerField('Число бариста на смене')

    class Meta:
        verbose_name = 'Кофейня'
        verbose_name_plural = 'Кофейни'
        ordering = ('barista_number', )

    def __str__(self):
        return self.address