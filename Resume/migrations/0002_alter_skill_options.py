# Generated by Django 4.0.5 on 2022-07-20 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['percent'], 'verbose_name': 'مهارت', 'verbose_name_plural': 'مهارت ها'},
        ),
    ]
