# Generated by Django 4.2.6 on 2023-10-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_article', models.CharField(max_length=250, verbose_name='Заголовок на странице со статьями')),
                ('img_title', models.ImageField(upload_to='static/upload_img/', verbose_name='img на странице со статьями')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='ЧПУ')),
                ('title', models.CharField(max_length=200, verbose_name='Блок title в html')),
                ('title_h1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице статьи')),
                ('img_article', models.ImageField(upload_to='static/upload_img/', verbose_name='img в статье')),
                ('description', models.TextField(verbose_name='Описание статьи')),
                ('canonical', models.TextField(verbose_name='canonical')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статья',
            },
        ),
    ]
