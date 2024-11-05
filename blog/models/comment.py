from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    commentator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments', verbose_name = 'Комментатор', )
    text = models.TextField('Текст комментария')
    likes = models.IntegerField('Количество лайков', default=0)
    create_datetime = models.DateTimeField('Дата и время создания комментария', auto_now_add=True)
    is_changed = models.BooleanField('Изменен ли комментарий', default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-create_datetime', )

    def __str__(self):
        return f'Комментарий @{self.commentator}'
