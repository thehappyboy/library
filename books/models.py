from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    subtitle = models.CharField(max_length=100, verbose_name='副标题')
    author = models.CharField(max_length=100, verbose_name='作者')
    isbn = models.CharField(max_length=13, verbose_name='ISBN', unique=True)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['title']

    def __str__(self):
        return self.title


