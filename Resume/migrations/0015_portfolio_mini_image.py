# Generated by Django 4.0.5 on 2022-07-28 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0014_categoryportfolio_portfolio_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='mini_image',
            field=models.ImageField(default=1, upload_to='images/Resume/portfolio/', verbose_name='تصویر کوچک نمونه کار'),
            preserve_default=False,
        ),
    ]
