from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce import models as tinymce_models
# Create your models here.

help_text = """
    Вставка img: ../../../../media/<название img> (в начале газрузить в админке)
    """

class News(models.Model):
    news = tinymce_models.HTMLField(verbose_name="Текст новости", help_text=help_text)

    def __str__(self):
        return self.news

    class Meta:
        verbose_name = "Новости на главной странице"
        verbose_name_plural = "Новости на главной странице"


class Article(models.Model):
    slug = models.SlugField(verbose_name="ЧПУ")
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_article = models.CharField(max_length=250, verbose_name="Заголовок на странице со статьями")
    img_title = models.ImageField(verbose_name="img на странице со статьями")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице статьи")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание статьи (блок 1)", help_text=help_text)

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"


class Reviews(models.Model):
    name = models.CharField(max_length=200, verbose_name="ФИ того, кто написал отзыв")
    review = tinymce_models.HTMLField(verbose_name="Отзыв", help_text=help_text)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


class Form(models.Model):
    phone_number = PhoneNumberField(null=False)
    time = models.CharField(max_length=25, verbose_name="Удобное время", null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name="Имя", null=True, blank=True)
    url = models.URLField(verbose_name="URL перехода", blank=True)

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"


class Project(models.Model):
    slug = models.SlugField(verbose_name="ЧПУ")
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_article = models.CharField(max_length=250, verbose_name="Заголовок на странице проектов")
    img_title = models.ImageField(verbose_name="img на странице проектов")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице проекта")
    img_article = models.ImageField(verbose_name="img в проекте")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    year = models.CharField(max_length=4, verbose_name='Год')
    name = tinymce_models.HTMLField(max_length=250, verbose_name='Название')
    address = tinymce_models.HTMLField(max_length=250, verbose_name='Адрес')
    design = tinymce_models.HTMLField(max_length=250, verbose_name='Дизайн конструкций')
    additionally = tinymce_models.HTMLField(verbose_name='Дополнительная информация')

    block = tinymce_models.HTMLField(verbose_name='Блок с фотографиями (+ текст)', help_text=help_text)

    def __str__(self):
        return self.title_h1_1

    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"



class Work_Example(models.Model):
    slug = models.SlugField(verbose_name="ЧПУ")
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_article = models.CharField(max_length=250, verbose_name="Заголовок на главной странице")
    img_title = models.ImageField(verbose_name="img на главной странице")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице примера работы")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)", help_text=help_text)

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Примеры работ на главной странице"
        verbose_name_plural = "Примеры работ на главной странице"


class Work_Example_In_Project(models.Model):
    slug = models.SlugField(verbose_name="ЧПУ")
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_article = models.CharField(max_length=250, verbose_name="Заголовок на странице с проектами")
    title_description = models.CharField(max_length=255, verbose_name="Краткое описание на странице с проектами")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице примера работы")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)", help_text=help_text)

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Примеры работ на странице с проектами"
        verbose_name_plural = "Примеры работ на странице с проектами"



class Main_menu_Model(models.Model):
    slug = models.SlugField(verbose_name="ЧПУ")
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)
    hide = models.BooleanField(default=False, verbose_name='Скрыть страницу в главном левом меню')

    name = models.CharField(max_length=100, verbose_name="Текст пункта в главном меню")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)", help_text=help_text)

    def __str__(self):
        return self.title_h1_1

    class Meta:
        verbose_name = "Главное левое меню"
        verbose_name_plural = "Главное левое меню"


class Image(models.Model):
    image = models.ImageField(verbose_name="img")

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Загрузка фото"
        verbose_name_plural = "Загрузка фото"


class Test(models.Model):
    text = models.CharField(max_length=2)

