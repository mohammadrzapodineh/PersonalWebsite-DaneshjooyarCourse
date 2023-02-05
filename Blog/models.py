from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from .managers import ArticleManager
from taggit.managers import TaggableManager
from jalali_date import datetime2jalali
from django.shortcuts import  reverse


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=120, verbose_name='عنوان مقاله', blank=True, null=True)
    description = RichTextUploadingField(verbose_name='متن مقاله')
    image = models.ImageField(upload_to='images/blog/article/', verbose_name='عکس مقاله')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت مقاله')
    active = models.BooleanField(default=False, verbose_name='نمایش داده شود یا نشود')
    # articles = models.Manager()
    objects = ArticleManager()
    # objects.all()
    tags = TaggableManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('Blog:blog_detail', args=[self.id])

    def __str__(self):
        return f'مقاله ی :{self.title}'

    def get_created_to_jalali(self):
        created_date = datetime2jalali(self.created).strftime('%Y/%m/%d')
        return created_date

    get_created_to_jalali.short_description='تاریخ ایجاد'

    def get_updated_to_jalali(self):
        updated_date = datetime2jalali(self.updated).strftime('%Y/%m/%d')
        return updated_date

    get_updated_to_jalali.short_description = 'تاریخ آپدیت'