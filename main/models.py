from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce import models as tinymce_models
# Create your models here.

help_text = '''
    Примеры тегов и классов: 
    <p>&lt;a href="#" class="link-text"&gt;&lt;/a&gt;</p>
    <p>&lt;p class="main-text with-margin"&gt;&lt;/p&gt;</p> 
    <p>&lt;h2 class="h2-title with-margin"&gt;&lt;/h2&gt;</p>
    <p>&lt;i&gt;&lt;/i&gt;</p>
    <p>&lt;b&gt;&lt;/b&gt;</p>
    <p></p><p></p>
    <p>навигация c элементами списка:</p>
    <p>&lt;nav class="only-text-block-list with-margin"&gt;</p>
    <p>&lt;li class="main-text"&gt;&lt;/li&gt;</p>
    <p>&lt;/nav&gt;</p>
    <p></p><p></p>
    <p>ссылка на форму обратной связи: </p>
    <p>&lt;a class=" link-text callback-btn"&gt;Отправить заявку&lt;/a&gt;</p>
    '''

class News(models.Model):
    news = tinymce_models.HTMLField(verbose_name="Текст новости")
    img = models.ImageField(upload_to="static/upload_img/", verbose_name="img в новости", blank=True, null=True)

    title = models.CharField(max_length=250, blank=True, null=True)
    alt = models.CharField(max_length=250, blank=True, null=True)

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
    img_title = models.ImageField(upload_to="static/upload_img/", verbose_name="img на странице со статьями")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице статьи")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img в статье")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание статьи (блок 1)")
    title_h1_2 = models.CharField(max_length=250, verbose_name="Второй заголовок (h2) на странице статьи для второго блока", blank=True, null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание статьи (блок 2 напротив img)", blank=True, null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание статьи (блок 3 под img) ", blank=True, null=True)

    title_img = models.CharField(max_length=250, blank=True, null=True)
    alt_img = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"


class Reviews(models.Model):
    name = models.CharField(max_length=200, verbose_name="ФИ того, кто написал отзыв")
    review = tinymce_models.HTMLField(verbose_name="Отзыв")

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

    title_article = models.CharField(max_length=250, verbose_name="Заголовок на странице со статьями")
    img_title = models.ImageField(upload_to="static/upload_img/", verbose_name="img на странице со статьями")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице статьи")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img в статье")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    year = models.CharField(max_length=4, verbose_name='Год')
    name = models.CharField(max_length=250, verbose_name='Название', help_text=help_text)
    address = models.CharField(max_length=250, verbose_name='Адрес')
    design = models.CharField(max_length=250, verbose_name='Дизайн конструкций', help_text=help_text)
    additionally = tinymce_models.HTMLField(verbose_name='Дополнительная информация')

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1", blank=True, null=True)
    img2 = models.ImageField(upload_to="static/upload_img/", verbose_name="img2", blank=True, null=True)
    img3 = models.ImageField(upload_to="static/upload_img/", verbose_name="img3", blank=True, null=True)
    img4 = models.ImageField(upload_to="static/upload_img/", verbose_name="img4", blank=True, null=True)
    img5 = models.ImageField(upload_to="static/upload_img/", verbose_name="img5", blank=True, null=True)
    img6 = models.ImageField(upload_to="static/upload_img/", verbose_name="img6", blank=True, null=True)
    img7 = models.ImageField(upload_to="static/upload_img/", verbose_name="img7", blank=True, null=True)
    img8 = models.ImageField(upload_to="static/upload_img/", verbose_name="img8", blank=True, null=True)
    img9 = models.ImageField(upload_to="static/upload_img/", verbose_name="img9", blank=True, null=True)
    img10 = models.ImageField(upload_to="static/upload_img/", verbose_name="img10", blank=True, null=True)
    img11 = models.ImageField(upload_to="static/upload_img/", verbose_name="img11", blank=True, null=True)
    img12 = models.ImageField(upload_to="static/upload_img/", verbose_name="img12", blank=True, null=True)

    title_img1 = models.CharField(max_length=250, blank=True, null=True)
    alt_img1 = models.CharField(max_length=250, blank=True, null=True)

    title_img2 = models.CharField(max_length=250, blank=True, null=True)
    alt_img2 = models.CharField(max_length=250, blank=True, null=True)

    title_img3 = models.CharField(max_length=250, blank=True, null=True)
    alt_img3 = models.CharField(max_length=250, blank=True, null=True)

    title_img4 = models.CharField(max_length=250, blank=True, null=True)
    alt_img4 = models.CharField(max_length=250, blank=True, null=True)

    title_img5 = models.CharField(max_length=250, blank=True, null=True)
    alt_img5 = models.CharField(max_length=250, blank=True, null=True)

    title_img6 = models.CharField(max_length=250, blank=True, null=True)
    alt_img6 = models.CharField(max_length=250, blank=True, null=True)

    title_img7 = models.CharField(max_length=250, blank=True, null=True)
    alt_img7 = models.CharField(max_length=250, blank=True, null=True)

    title_img8 = models.CharField(max_length=250, blank=True, null=True)
    alt_img8 = models.CharField(max_length=250, blank=True, null=True)

    title_img9 = models.CharField(max_length=250, blank=True, null=True)
    alt_img9 = models.CharField(max_length=250, blank=True, null=True)

    title_img10 = models.CharField(max_length=250, blank=True, null=True)
    alt_img10 = models.CharField(max_length=250, blank=True, null=True)

    title_img11 = models.CharField(max_length=250, blank=True, null=True)
    alt_img11 = models.CharField(max_length=250, blank=True, null=True)

    title_img12 = models.CharField(max_length=250, blank=True, null=True)
    alt_img12 = models.CharField(max_length=250, blank=True, null=True)

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
    img_title = models.ImageField(upload_to="static/upload_img/", verbose_name="img на главной странице")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице примера работы")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    description_2 = tinymce_models.HTMLField(verbose_name="Описание в рамке (блок 2) ")

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True, null=True)
    img2 = models.ImageField(upload_to="static/upload_img/", verbose_name="img2", blank=True, null=True)
    img3 = models.ImageField(upload_to="static/upload_img/", verbose_name="img3", blank=True, null=True)
    img4 = models.ImageField(upload_to="static/upload_img/", verbose_name="img4", blank=True, null=True)
    img5 = models.ImageField(upload_to="static/upload_img/", verbose_name="img5", blank=True, null=True)
    img6 = models.ImageField(upload_to="static/upload_img/", verbose_name="img6", blank=True, null=True)
    img7 = models.ImageField(upload_to="static/upload_img/", verbose_name="img7", blank=True, null=True)
    img8 = models.ImageField(upload_to="static/upload_img/", verbose_name="img8", blank=True, null=True)
    img9 = models.ImageField(upload_to="static/upload_img/", verbose_name="img9", blank=True, null=True)
    img10 = models.ImageField(upload_to="static/upload_img/", verbose_name="img10", blank=True, null=True)
    img11 = models.ImageField(upload_to="static/upload_img/", verbose_name="img11", blank=True, null=True)
    img12 = models.ImageField(upload_to="static/upload_img/", verbose_name="img12", blank=True, null=True)

    title_img1 = models.CharField(max_length=250, blank=True, null=True)
    alt_img1 = models.CharField(max_length=250, blank=True, null=True)

    title_img2 = models.CharField(max_length=250, blank=True, null=True)
    alt_img2 = models.CharField(max_length=250, blank=True, null=True)

    title_img3 = models.CharField(max_length=250, blank=True, null=True)
    alt_img3 = models.CharField(max_length=250, blank=True, null=True)

    title_img4 = models.CharField(max_length=250, blank=True, null=True)
    alt_img4 = models.CharField(max_length=250, blank=True, null=True)

    title_img5 = models.CharField(max_length=250, blank=True, null=True)
    alt_img5 = models.CharField(max_length=250, blank=True, null=True)

    title_img6 = models.CharField(max_length=250, blank=True, null=True)
    alt_img6 = models.CharField(max_length=250, blank=True, null=True)

    title_img7 = models.CharField(max_length=250, blank=True, null=True)
    alt_img7 = models.CharField(max_length=250, blank=True, null=True)

    title_img8 = models.CharField(max_length=250, blank=True, null=True)
    alt_img8 = models.CharField(max_length=250, blank=True, null=True)

    title_img9 = models.CharField(max_length=250, blank=True, null=True)
    alt_img9 = models.CharField(max_length=250, blank=True, null=True)

    title_img10 = models.CharField(max_length=250, blank=True, null=True)
    alt_img10 = models.CharField(max_length=250, blank=True, null=True)

    title_img11 = models.CharField(max_length=250, blank=True, null=True)
    alt_img11 = models.CharField(max_length=250, blank=True, null=True)

    title_img12 = models.CharField(max_length=250, blank=True, null=True)
    alt_img12 = models.CharField(max_length=250, blank=True, null=True)

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
    title_description = tinymce_models.HTMLField(max_length=350, verbose_name="Краткое описание на странице с проектами")

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1) на странице примера работы")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    description_2 = tinymce_models.HTMLField(verbose_name="Описание в рамке (блок 2)")


    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True, null=True)
    img2 = models.ImageField(upload_to="static/upload_img/", verbose_name="img2", blank=True, null=True)
    img3 = models.ImageField(upload_to="static/upload_img/", verbose_name="img3", blank=True, null=True)
    img4 = models.ImageField(upload_to="static/upload_img/", verbose_name="img4", blank=True, null=True)
    img5 = models.ImageField(upload_to="static/upload_img/", verbose_name="img5", blank=True, null=True)
    img6 = models.ImageField(upload_to="static/upload_img/", verbose_name="img6", blank=True, null=True)
    img7 = models.ImageField(upload_to="static/upload_img/", verbose_name="img7", blank=True, null=True)
    img8 = models.ImageField(upload_to="static/upload_img/", verbose_name="img8", blank=True, null=True)
    img9 = models.ImageField(upload_to="static/upload_img/", verbose_name="img9", blank=True, null=True)
    img10 = models.ImageField(upload_to="static/upload_img/", verbose_name="img10", blank=True, null=True)
    img11 = models.ImageField(upload_to="static/upload_img/", verbose_name="img11", blank=True, null=True)
    img12 = models.ImageField(upload_to="static/upload_img/", verbose_name="img12", blank=True, null=True)

    title_img1 = models.CharField(max_length=250, blank=True, null=True)
    alt_img1 = models.CharField(max_length=250, blank=True, null=True)

    title_img2 = models.CharField(max_length=250, blank=True, null=True)
    alt_img2 = models.CharField(max_length=250, blank=True, null=True)

    title_img3 = models.CharField(max_length=250, blank=True, null=True)
    alt_img3 = models.CharField(max_length=250, blank=True, null=True)

    title_img4 = models.CharField(max_length=250, blank=True, null=True)
    alt_img4 = models.CharField(max_length=250, blank=True, null=True)

    title_img5 = models.CharField(max_length=250, blank=True, null=True)
    alt_img5 = models.CharField(max_length=250, blank=True, null=True)

    title_img6 = models.CharField(max_length=250, blank=True, null=True)
    alt_img6 = models.CharField(max_length=250, blank=True, null=True)

    title_img7 = models.CharField(max_length=250, blank=True, null=True)
    alt_img7 = models.CharField(max_length=250, blank=True, null=True)

    title_img8 = models.CharField(max_length=250, blank=True, null=True)
    alt_img8 = models.CharField(max_length=250, blank=True, null=True)

    title_img9 = models.CharField(max_length=250, blank=True, null=True)
    alt_img9 = models.CharField(max_length=250, blank=True, null=True)

    title_img10 = models.CharField(max_length=250, blank=True, null=True)
    alt_img10 = models.CharField(max_length=250, blank=True, null=True)

    title_img11 = models.CharField(max_length=250, blank=True, null=True)
    alt_img11 = models.CharField(max_length=250, blank=True, null=True)

    title_img12 = models.CharField(max_length=250, blank=True, null=True)
    alt_img12 = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Примеры работ на странице с проектами"
        verbose_name_plural = "Примеры работ на странице с проектами"








