# Generated by Django 4.0.5 on 2022-07-20 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0002_alter_skill_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['-percent'], 'verbose_name': 'مهارت', 'verbose_name_plural': 'مهارت ها'},
        ),
    ]
