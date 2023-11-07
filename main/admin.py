from django.contrib import admin
from main.models import Article, News, Reviews, Form, Project, Work_Example, Work_Example_In_Project
# Register your models here.

admin.site.register(Form)
admin.site.register(News)
admin.site.register(Reviews)


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
            'fields': ('title_h1_1', 'img_article', 'year', 'name', 'address', 'design', 'additionally'),
        }),
        ('Блок фото', {
            'fields': ('img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8', 'img9', 'img10', 'img11', 'img12'),
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
    )
admin.site.register(Work_Example_In_Project, Work_Example_In_ProjectAdmin)