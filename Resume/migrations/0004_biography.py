# Generated by Django 4.0.5 on 2022-07-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0003_alter_skill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='', verbose_name='توصیر آواتار کاربر')),
                ('description', models.TextField(verbose_name='متن بیوگرافی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال باشد؟')),
            ],
            options={
                'verbose_name': 'بیوگرافی',
                'verbose_name_plural': 'بیوگرافی ها',
            },
        ),
    ]
