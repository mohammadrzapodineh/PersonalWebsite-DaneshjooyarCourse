from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان اسلایدر')
    description = models.CharField(max_length=200, verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders/', verbose_name='تصویر اسلایدر')
    url = models.URLField(verbose_name='آدرس اسلایدر')
    is_show = models.BooleanField(default=False, verbose_name='نمایش داده شود؟')
    fade_up_image = models.ImageField(upload_to='images/sliders/fades/', verbose_name='تصویر متحرک', default='image.png')

    class Meta:
        ordering = ['-title', 'is_show']
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return f'Slider:{self.title}'



