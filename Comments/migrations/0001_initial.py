# Generated by Django 4.0.5 on 2022-08-04 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blog', '0002_article_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='نام فرستنده کامنت')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل فرستنده کامنت')),
                ('text', models.TextField(verbose_name='متن کامنت')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True, verbose_name='نمایش داده شود یا نشود')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.article')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
            },
        ),
    ]