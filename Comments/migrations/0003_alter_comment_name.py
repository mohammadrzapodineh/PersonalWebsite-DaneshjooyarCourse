# Generated by Django 4.0.5 on 2022-08-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0002_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=140, verbose_name='نام فرستنده کامنت'),
        ),
    ]
