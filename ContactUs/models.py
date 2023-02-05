from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=110, verbose_name='نام کاربر')
    subject = models.CharField(max_length=150, verbose_name='عنوان پیام کاربر')
    email = models.EmailField(verbose_name='ایمیل کاربر')
    text = models.TextField(verbose_name='پیفام کاربر', max_length=500)

    class Meta:
        verbose_name = 'پیفام کاربر'
        verbose_name_plural = 'پیغام های کاربران'

    def __str__(self):
        return f'پیفام از طرف :{self.name}'