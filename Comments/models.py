from django.db import models
from Blog.models import Article


class Comment(models.Model):
    name = models.CharField(verbose_name='نام فرستنده کامنت', max_length=140)
    email = models.EmailField(verbose_name='ایمیل فرستنده کامنت')
    text = models.TextField(verbose_name='متن کامنت')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='نمایش داده شود یا نشود')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f' کامنت :{self.name}- مقاله  :{self.article.title}'

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

