# Generated by Django 4.2.6 on 2023-11-16 20:12

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
                ('img_title', models.ImageField(upload_to='static/media/', verbose_name='img на странице со статьями')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице статьи')),
                ('img_article', models.ImageField(upload_to='static/media/', verbose_name='img в статье')),
                ('description_1', tinymce.models.HTMLField(verbose_name='Описание статьи (блок 1)')),
                ('title_h1_2', models.CharField(blank=True, max_length=250, null=True, verbose_name='Второй заголовок (h2) на странице статьи для второго блока')),
                ('description_2', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание статьи (блок 2 напротив img)')),
                ('description_3', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание статьи (блок 3 под img) ')),
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
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', tinymce.models.HTMLField(verbose_name='Текст новости')),
                ('img', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img в новости')),
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
                ('title_article', models.CharField(max_length=250, verbose_name='Заголовок на странице со статьями')),
                ('img_title', models.ImageField(upload_to='static/media/', verbose_name='img на странице со статьями')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице статьи')),
                ('img_article', models.ImageField(upload_to='static/media/', verbose_name='img в статье')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('name', models.CharField(help_text='\n    Примеры тегов и классов: \n    <p>&lt;a href="#" class="link-text"&gt;&lt;/a&gt;</p>\n    <p>&lt;p class="main-text with-margin"&gt;&lt;/p&gt;</p> \n    <p>&lt;h2 class="h2-title with-margin"&gt;&lt;/h2&gt;</p>\n    <p>&lt;i&gt;&lt;/i&gt;</p>\n    <p>&lt;b&gt;&lt;/b&gt;</p>\n    <p></p><p></p>\n    <p>навигация c элементами списка:</p>\n    <p>&lt;nav class="only-text-block-list with-margin"&gt;</p>\n    <p>&lt;li class="main-text"&gt;&lt;/li&gt;</p>\n    <p>&lt;/nav&gt;</p>\n    <p></p><p></p>\n    <p>ссылка на форму обратной связи: </p>\n    <p>&lt;a class=" link-text callback-btn"&gt;Отправить заявку&lt;/a&gt;</p>\n    ', max_length=250, verbose_name='Название')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('design', models.CharField(help_text='\n    Примеры тегов и классов: \n    <p>&lt;a href="#" class="link-text"&gt;&lt;/a&gt;</p>\n    <p>&lt;p class="main-text with-margin"&gt;&lt;/p&gt;</p> \n    <p>&lt;h2 class="h2-title with-margin"&gt;&lt;/h2&gt;</p>\n    <p>&lt;i&gt;&lt;/i&gt;</p>\n    <p>&lt;b&gt;&lt;/b&gt;</p>\n    <p></p><p></p>\n    <p>навигация c элементами списка:</p>\n    <p>&lt;nav class="only-text-block-list with-margin"&gt;</p>\n    <p>&lt;li class="main-text"&gt;&lt;/li&gt;</p>\n    <p>&lt;/nav&gt;</p>\n    <p></p><p></p>\n    <p>ссылка на форму обратной связи: </p>\n    <p>&lt;a class=" link-text callback-btn"&gt;Отправить заявку&lt;/a&gt;</p>\n    ', max_length=250, verbose_name='Дизайн конструкций')),
                ('additionally', tinymce.models.HTMLField(verbose_name='Дополнительная информация')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img4')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img5')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img6')),
                ('img7', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img7')),
                ('img8', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img8')),
                ('img9', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img9')),
                ('img10', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img10')),
                ('img11', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img11')),
                ('img12', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img12')),
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
                ('review', tinymce.models.HTMLField(verbose_name='Отзыв')),
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
                ('img_title', models.ImageField(upload_to='static/media/', verbose_name='img на главной странице')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице примера работы')),
                ('description_1', tinymce.models.HTMLField(verbose_name='Описание (блок 1)')),
                ('description_2', tinymce.models.HTMLField(verbose_name='Описание в рамке (блок 2) ')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img4')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img5')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img6')),
                ('img7', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img7')),
                ('img8', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img8')),
                ('img9', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img9')),
                ('img10', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img10')),
                ('img11', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img11')),
                ('img12', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img12')),
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
                ('title_description', models.TextField(help_text='\n    Примеры тегов и классов: \n    <p>&lt;a href="#" class="link-text"&gt;&lt;/a&gt;</p>\n    <p>&lt;p class="main-text with-margin"&gt;&lt;/p&gt;</p> \n    <p>&lt;h2 class="h2-title with-margin"&gt;&lt;/h2&gt;</p>\n    <p>&lt;i&gt;&lt;/i&gt;</p>\n    <p>&lt;b&gt;&lt;/b&gt;</p>\n    <p></p><p></p>\n    <p>навигация c элементами списка:</p>\n    <p>&lt;nav class="only-text-block-list with-margin"&gt;</p>\n    <p>&lt;li class="main-text"&gt;&lt;/li&gt;</p>\n    <p>&lt;/nav&gt;</p>\n    <p></p><p></p>\n    <p>ссылка на форму обратной связи: </p>\n    <p>&lt;a class=" link-text callback-btn"&gt;Отправить заявку&lt;/a&gt;</p>\n    ', max_length=350, verbose_name='Краткое описание на странице с проектами')),
                ('title_h1_1', models.CharField(max_length=250, verbose_name='Заголовок (h1) на странице примера работы')),
                ('description_1', tinymce.models.HTMLField(verbose_name='Описание (блок 1)')),
                ('description_2', tinymce.models.HTMLField(verbose_name='Описание в рамке (блок 2)')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img1 (загружать подряд по две)')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img4')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img5')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img6')),
                ('img7', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img7')),
                ('img8', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img8')),
                ('img9', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img9')),
                ('img10', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img10')),
                ('img11', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img11')),
                ('img12', models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='img12')),
            ],
            options={
                'verbose_name': 'Примеры работ на странице с проектами',
                'verbose_name_plural': 'Примеры работ на странице с проектами',
            },
        ),
    ]
