from django.contrib import admin
from main.models import Article, News, Reviews, Form, Project, Work_Example, Work_Example_In_Project, \
    Main_menu_Model, Image

# Register your models here.


admin.site.register(Form)
admin.site.register(Reviews)
admin.site.register(News)
admin.site.register(Image)


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('meta', {
            'fields': ('slug', 'title', 'canonical', 'description'),
        }),
        ('Статья на странице со статьями (превью)', {
            'fields': ('title_article', 'img_title'),
        }),
        ('Статья', {
            'fields': ('title_h1_1', 'description_1',),
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
        ('Информация проекта', {
            'fields': (
            'title_h1_1', 'img_article', 'alt_img_article', 'title_img_article', 'year', 'name', 'address', 'design',
            'additionally'),
        }),
        ('Блок под информацией', {
            'fields': ('block',),
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
            'fields': ('title_h1_1', 'description_1'),
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
            'fields': ('title_h1_1', 'description_1'),
        }),
    )
admin.site.register(Work_Example_In_Project, Work_Example_In_ProjectAdmin)


class Main_menuAdmin(admin.ModelAdmin):
    fieldsets = (
        ('meta', {
            'fields': ('slug', 'title', 'canonical', 'description', 'hide'),
        }),
        ('Текст пункта', {
            'fields': ('name',),
        }),
        ('Страница', {
            'fields': ('title_h1_1', 'description_1'),
        }),
    )
admin.site.register(Main_menu_Model, Main_menuAdmin)
