from django.db import models


class Setting(models.Model):
    email = models.EmailField(verbose_name='ایمیل مجموعه')
    copy_right_text = models.CharField(max_length=120, verbose_name='متن کپی رایت')
    address = models.CharField(max_length=400, verbose_name='آدرس مجموعه')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس مجموعه')
    map_address = models.CharField(verbose_name='آدرس مجموعه در گوگل مپ', blank=True, max_length=500)

    class Meta:
        verbose_name = 'تنظیمات وبسایت '
        verbose_name_plural = 'تنظیمات وبسایت'

    def __str__(self):
        return f'تنظیمات:{self.id}'


class SocialMedia(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان شبکه اجتماعی ')
    url = models.URLField(verbose_name='آدرس شبکه اجتماعی')
    SOCIAL_MEDIA_ICONS = [
        ('facebook', 'آیکونfacebook  '),
        ('twitter', 'آیکون twitter  '),
        ('google-plus', 'آیکونgoogle-plus   '),
        ('linkedin', 'آیکونlinkedin  '),
        ('facebook', 'آیکونpinterest  ')
    ]
    icon = models.CharField(max_length=15, verbose_name='آیکون شبکه اجتماعی ', choices=SOCIAL_MEDIA_ICONS)

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'

    def __str__(self):
        return f'شبکه ی اجتماعی:{self.title}'
