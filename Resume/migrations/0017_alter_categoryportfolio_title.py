# Generated by Django 4.0.5 on 2022-07-30 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0016_remove_portfolio_image_portfolio_big_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryportfolio',
            name='title',
            field=models.CharField(max_length=110, unique=True, verbose_name='عنوان دسته بندی'),
        ),
    ]
