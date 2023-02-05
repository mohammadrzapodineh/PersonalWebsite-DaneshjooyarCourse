# Generated by Django 4.0.5 on 2022-07-20 21:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0004_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percent',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator('مقدار وارد شده بیشتر از حد مجاز است'), django.core.validators.MinValueValidator('مقدار وارد شده کمتر از حد مجاز است')], verbose_name='درصد تسلط بر مهارت'),
        ),
    ]
