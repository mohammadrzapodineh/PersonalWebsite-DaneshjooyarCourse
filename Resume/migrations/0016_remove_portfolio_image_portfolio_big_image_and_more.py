# Generated by Django 4.0.5 on 2022-07-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0015_portfolio_mini_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='image',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='big_image',
            field=models.ImageField(default=1, upload_to='images/Resume/portfolio/', verbose_name='تصویربزرگ نمونه کار'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='mini_image',
            field=models.ImageField(upload_to='images/Resume/portfolio/', verbose_name='تصویر  کوچک نمونه کار'),
        ),
    ]