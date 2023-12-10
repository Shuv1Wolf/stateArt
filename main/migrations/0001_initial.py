# Generated by Django 4.2.6 on 2023-12-10 16:21

from django.db import migrations, models
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='ЧПУ')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('canonical', models.CharField(blank=True, max_length=255, null=True, verbose_name='canonical')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('title_article', models.CharField(max_length=250, verbose_name='Заголовок на странице со статьями')),
                ('img_title', models.ImageField(upload_to='', verbose_name='img на странице со статьями')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице статьи')),
                ('description_1', tinymce.models.HTMLField(help_text='\n    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)\n    ', verbose_name='Описание статьи (блок 1)')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статья',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('time', models.CharField(blank=True, max_length=25, null=True, verbose_name='Удобное время')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Имя')),
                ('url', models.URLField(blank=True, verbose_name='URL перехода')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='img')),
            ],
            options={
                'verbose_name': 'Загрузка фото',
                'verbose_name_plural': 'Загрузка фото',
            },
        ),
        migrations.CreateModel(
            name='Main_menu_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='ЧПУ')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('canonical', models.CharField(blank=True, max_length=255, null=True, verbose_name='canonical')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('hide', models.BooleanField(default=False, verbose_name='Скрыть страницу в главном левом меню')),
                ('name', models.CharField(max_length=100, verbose_name='Текст пункта в главном меню')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1)')),
                ('description_1', tinymce.models.HTMLField(help_text='\n    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)\n    ', verbose_name='Описание (блок 1)')),
            ],
            options={
                'verbose_name': 'Главное левое меню',
                'verbose_name_plural': 'Главное левое меню',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', tinymce.models.HTMLField(help_text='\n    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)\n    ', verbose_name='Текст новости')),
            ],
            options={
                'verbose_name': 'Новости на главной странице',
                'verbose_name_plural': 'Новости на главной странице',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='ЧПУ')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('canonical', models.CharField(blank=True, max_length=255, null=True, verbose_name='canonical')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('title_article', models.CharField(max_length=250, verbose_name='Заголовок на странице проектов')),
                ('img_title', models.ImageField(upload_to='', verbose_name='img на странице проектов')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице проекта')),
                ('img_article', models.ImageField(upload_to='', verbose_name='img в проекте')),
                ('alt_img_article', models.CharField(blank=True, max_length=250, null=True, verbose_name="SEO alt 'img в статье'")),
                ('title_img_article', models.CharField(blank=True, max_length=250, null=True, verbose_name="SEO title 'img в статье'")),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('name', tinymce.models.HTMLField(max_length=250, verbose_name='Название')),
                ('address', tinymce.models.HTMLField(max_length=250, verbose_name='Адрес')),
                ('design', tinymce.models.HTMLField(max_length=250, verbose_name='Дизайн конструкций')),
                ('additionally', tinymce.models.HTMLField(verbose_name='Дополнительная информация')),
                ('block', tinymce.models.HTMLField(help_text='\n    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)\n    ', verbose_name='Блок с фотографиями (+ текст)')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИ того, кто написал отзыв')),
                ('review', tinymce.models.HTMLField(help_text='\n    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)\n    ', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Work_Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='ЧПУ')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('canonical', models.CharField(blank=True, max_length=255, null=True, verbose_name='canonical')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('title_article', models.CharField(max_length=250, verbose_name='Заголовок на главной странице')),
                ('img_title', models.ImageField(upload_to='', verbose_name='img на главной странице')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице примера работы')),
                ('description_1', tinymce.models.HTMLField(help_text='\n    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)\n    ', verbose_name='Описание (блок 1)')),
            ],
            options={
                'verbose_name': 'Примеры работ на главной странице',
                'verbose_name_plural': 'Примеры работ на главной странице',
            },
        ),
        migrations.CreateModel(
            name='Work_Example_In_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='ЧПУ')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('canonical', models.CharField(blank=True, max_length=255, null=True, verbose_name='canonical')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('title_article', models.CharField(max_length=250, verbose_name='Заголовок на странице с проектами')),
                ('title_description', models.CharField(max_length=255, verbose_name='Краткое описание на странице с проектами')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице примера работы')),
                ('description_1', tinymce.models.HTMLField(help_text='\n    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)\n    ', verbose_name='Описание (блок 1)')),
            ],
            options={
                'verbose_name': 'Примеры работ на странице с проектами',
                'verbose_name_plural': 'Примеры работ на странице с проектами',
            },
        ),
    ]