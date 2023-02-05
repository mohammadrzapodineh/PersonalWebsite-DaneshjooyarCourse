from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import max_value_validator, min_value_validator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Skill(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان مهارت')
    percent = models.IntegerField(verbose_name='درصد تسلط بر مهارت',validators=[max_value_validator, min_value_validator])

    class Meta:
        ordering = ['-percent']
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return f'مهارت:{self.title}'


class Biography(models.Model):
    avatar = models.ImageField(verbose_name='توصیر آواتار کاربر')
    description = RichTextField(verbose_name='توضیح بیوگرافی')
    is_active = models.BooleanField(verbose_name='فعال باشد؟', default=False)

    class Meta:
        verbose_name = 'بیوگرافی'
        verbose_name_plural = 'بیوگرافی ها'

    def __str__(self):
        return f'بیوگرافی:'


class Experience(models.Model):
    projects_count = models.IntegerField(verbose_name='تعداد پروژه های موفق')
    working_hours = models.IntegerField(verbose_name='تعداد ساعات کار')
    rates = models.IntegerField(verbose_name='تعداد امتیاز های کاربران')
    customers = models.IntegerField(verbose_name='تعداد مشتری های شما')

    class Meta:
        verbose_name = 'تجربه'
        verbose_name_plural = 'تجربه ها'

    def __str__(self):
        return f'تجربه:{self.id}'


class Portfolio(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان نمونه کار')
    big_image = models.ImageField(verbose_name='تصویربزرگ نمونه کار', upload_to='images/Resume/portfolio/')
    mini_image = models.ImageField(verbose_name='تصویر  کوچک نمونه کار', upload_to='images/Resume/portfolio/')
    categories = models.ManyToManyField('CategoryPortfolio', verbose_name='دسته بندی')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کار ها'

    def __str__(self):
        return self.title


class CategoryPortfolio(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان دسته بندی', unique=True)

    class Meta:
        ordering = ('-title',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی  ها'

    def __str__(self):
        return self.title