from django.contrib import admin
from main.models import Article, News, Reviews, Form, Project, Work_Example, Work_Example_In_Project
# Register your models here.


admin.site.register(Form)
admin.site.register(Reviews)

class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Новость', {
            'fields': ('news', 'img'),
        }),
        ('SEO in img', {
            'fields': ('title', 'alt'),
        }),

    )
admin.site.register(News, NewsAdmin)


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('meta', {
            'fields': ('slug', 'title', 'canonical', 'description'),
        }),
        ('Статья на странице со статьями (превью)', {
            'fields': ('title_article', 'img_title'),
        }),
        ('Статья', {
            'fields': ('title_h1_1', 'img_article', 'description_1', 'title_h1_2', 'description_2', 'description_3'),
        }),
        ('SEO in img', {
            'fields': ('title_img', 'alt_img'),
        }),
    )
admin.site.register(Article, ArticleAdmin)


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('meta', {
            'fields': ('slug', 'title', 'canonical', 'description'),
        }),
        ('Проект на странице с проектами (превью)', {
            'fields': ('title_article', 'img_title'),
        }),
        ('Проект', {
            'fields': ('title_h1_1', 'img_article', 'alt_img_article', 'title_img_article', 'year', 'name', 'address', 'design', 'additionally'),
        }),
        ('Блок фото', {
            'fields': ('img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8', 'img9', 'img10', 'img11', 'img12'),
        }),
        ('SEO in img1', {
            'fields': ('title_img1', 'alt_img1'),
        }),
        ('SEO in img2', {
            'fields': ('title_img2', 'alt_img2'),
        }),
        ('SEO in img3', {
            'fields': ('title_img3', 'alt_img3'),
        }),
        ('SEO in img4', {
            'fields': ('title_img4', 'alt_img4'),
        }),
        ('SEO in img5', {
            'fields': ('title_img5', 'alt_img5'),
        }),
        ('SEO in img6', {
            'fields': ('title_img6', 'alt_img6'),
        }),
        ('SEO in img7', {
            'fields': ('title_img7', 'alt_img7'),
        }),
        ('SEO in img8', {
            'fields': ('title_img8', 'alt_img8'),
        }),
        ('SEO in img9', {
            'fields': ('title_img9', 'alt_img9'),
        }),
        ('SEO in img10', {
            'fields': ('title_img10', 'alt_img10'),
        }),
        ('SEO in img11', {
            'fields': ('title_img11', 'alt_img11'),
        }),
        ('SEO in img12', {
            'fields': ('title_img12', 'alt_img12'),
        }),
    )
admin.site.register(Project, ProjectAdmin)


class Work_ExampleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('meta', {
            'fields': ('slug', 'title', 'canonical', 'description'),
        }),
        ('Пример работ на главной странице (превью)', {
            'fields': ('title_article', 'img_title'),
        }),
        ('Пример работ', {
            'fields': ('title_h1_1', 'description_1', 'description_2'),
        }),
        ('Блок фото (загружать по 2)', {
            'fields': ('img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8', 'img9', 'img10', 'img11', 'img12'),
        }),
        ('SEO in img1', {
            'fields': ('title_img1', 'alt_img1'),
        }),
        ('SEO in img2', {
            'fields': ('title_img2', 'alt_img2'),
        }),
        ('SEO in img3', {
            'fields': ('title_img3', 'alt_img3'),
        }),
        ('SEO in img4', {
            'fields': ('title_img4', 'alt_img4'),
        }),
        ('SEO in img5', {
            'fields': ('title_img5', 'alt_img5'),
        }),
        ('SEO in img6', {
            'fields': ('title_img6', 'alt_img6'),
        }),
        ('SEO in img7', {
            'fields': ('title_img7', 'alt_img7'),
        }),
        ('SEO in img8', {
            'fields': ('title_img8', 'alt_img8'),
        }),
        ('SEO in img9', {
            'fields': ('title_img9', 'alt_img9'),
        }),
        ('SEO in img10', {
            'fields': ('title_img10', 'alt_img10'),
        }),
        ('SEO in img11', {
            'fields': ('title_img11', 'alt_img11'),
        }),
        ('SEO in img12', {
            'fields': ('title_img12', 'alt_img12'),
        }),
    )
admin.site.register(Work_Example, Work_ExampleAdmin)


class Work_Example_In_ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('meta', {
            'fields': ('slug', 'title', 'canonical', 'description'),
        }),
        ('Пример работ на странице с проектами (превью)', {
            'fields': ('title_article', 'title_description'),
        }),
        ('Пример работ', {
            'fields': ('title_h1_1', 'description_1', 'description_2'),
        }),
        ('Блок фото (загружать по 2)', {
            'fields': ('img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8', 'img9', 'img10', 'img11', 'img12'),
        }),
        ('SEO in img1', {
            'fields': ('title_img1', 'alt_img1'),
        }),
        ('SEO in img2', {
            'fields': ('title_img2', 'alt_img2'),
        }),
        ('SEO in img3', {
            'fields': ('title_img3', 'alt_img3'),
        }),
        ('SEO in img4', {
            'fields': ('title_img4', 'alt_img4'),
        }),
        ('SEO in img5', {
            'fields': ('title_img5', 'alt_img5'),
        }),
        ('SEO in img6', {
            'fields': ('title_img6', 'alt_img6'),
        }),
        ('SEO in img7', {
            'fields': ('title_img7', 'alt_img7'),
        }),
        ('SEO in img8', {
            'fields': ('title_img8', 'alt_img8'),
        }),
        ('SEO in img9', {
            'fields': ('title_img9', 'alt_img9'),
        }),
        ('SEO in img10', {
            'fields': ('title_img10', 'alt_img10'),
        }),
        ('SEO in img11', {
            'fields': ('title_img11', 'alt_img11'),
        }),
        ('SEO in img12', {
            'fields': ('title_img12', 'alt_img12'),
        }),
    )
admin.site.register(Work_Example_In_Project, Work_Example_In_ProjectAdmin)