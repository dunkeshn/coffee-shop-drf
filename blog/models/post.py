from django.db import models
from django.contrib.auth.models import User

from blog.models.comment import Comment


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts', verbose_name = 'Автор', )
    title = models.CharField('Название статьи', max_length=100)
    text = models.TextField('Текст статьи')
    image = models.ImageField('Фото статьи', blank=True, null=True)
    comments = models.ManyToManyField(to=Comment, related_name='posts', verbose_name='Комментарии', blank=True, null=True)
    likes = models.IntegerField('Количество лайков', default=0)
    create_datetime = models.DateTimeField('Дата и время создания комментария', auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-create_datetime', )

    def __str__(self):
        return f'Статья "{self.title}" - автор: {self.author}'