# Generated by Django 4.0.5 on 2022-07-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting', '0002_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.CharField(choices=[('facebook', 'آیکونfacebook  '), ('twitter', 'آیکون twitter  '), ('google-plus', 'آیکونgoogle-plus   '), ('linkedin', 'آیکونlinkedin  '), ('facebook', 'آیکونpinterest  ')], max_length=15, verbose_name='آیکون شبکه اجتماعی '),
        ),
    ]
