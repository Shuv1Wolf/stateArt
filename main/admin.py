from django.contrib import admin
from main.models import Article, News, Reviews, Form, Project, Work_Example
# Register your models here.

admin.site.register(Form)
admin.site.register(Article)
admin.site.register(News)
admin.site.register(Reviews)
admin.site.register(Project)
admin.site.register(Work_Example)