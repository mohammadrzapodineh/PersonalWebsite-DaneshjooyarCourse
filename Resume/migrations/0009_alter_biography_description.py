# Generated by Django 4.0.5 on 2022-07-20 22:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0008_alter_biography_description_alter_skill_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیح بیوگرافی'),
        ),
    ]
