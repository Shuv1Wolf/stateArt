from django.db import models
# Create your models here.

class News(models.Model):
    news = models.TextField(verbose_name="Текст новости")
    img = models.ImageField(upload_to="static/upload_img/", verbose_name="img в новости", blank=True, null=True)

    def __str__(self):
        return self.news

    class Meta:
        verbose_name = "Новости на главной странице"
        verbose_name_plural = "Новости на главной странице"


class Article(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True, verbose_name="ЧПУ")
    title = models.CharField(max_length=200, verbose_name="Блок title в html")

    title_article = models.CharField(max_length=250, verbose_name="Заголовок на странице со статьями")
    img_title = models.ImageField(upload_to="static/upload_img/", verbose_name="img на странице со статьями")

    title_h1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице статьи")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img в статье")
    description_1 = models.TextField(verbose_name="Описание статьи (блок 1)")
    description_2 = models.TextField(verbose_name="Описание статьи (блок 2 напротив img) ")
    description_3 = models.TextField(verbose_name="Описание статьи (блок 3 под img) ")
    canonical = models.TextField(verbose_name="canonical")  #для чего?

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"


class Reviews(models.Model):
    name = models.CharField(max_length=200, verbose_name="ФИ того, кто написал отзыв")
    review = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


class Form(models.Model):
    phone_number = models.CharField(max_length=17, blank=True, verbose_name="Номер телефона")
    time = models.TimeField(verbose_name="Удобное время",
                            error_messages="Time must be entered in the format: '00:00'")
    name = models.CharField(max_length=250, verbose_name="Имя")

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"



