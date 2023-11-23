from django.db import models
from tinymce import models as tinymce_models
# Create your models here.

##################################################
class Production_and_metalworking(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Производство и металлообработка"
        verbose_name_plural = "Производство и металлообработка"


class Our_workshop(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Наш цех"
        verbose_name_plural = "Наш цех"


class Bar_counters_and_reception(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Барные стойки и ресепшен"
        verbose_name_plural = "Барные стойки и ресепшен"


class Сanopies_and_canopies(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Навесы и козырьки"
        verbose_name_plural = "Навесы и козырьки"


class Furniture_and_interior_elements(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Мебель и элементы интерьера"
        verbose_name_plural = "Мебель и элементы интерьера"


class Entrances_and_doors(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Вход и двери"
        verbose_name_plural = "Вход и двери"


class Trusses_and_frames(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Фермы и каркасы"
        verbose_name_plural = "Фермы и каркасы"


class Colums(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Колонны"
        verbose_name_plural = "Колонны"


class Perforated_sheet_metal_structures(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Конструкции из перфолиста"
        verbose_name_plural = "Конструкции из перфолиста"


class Decorative_fasteners(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = "Декоративный крепеж"
        verbose_name_plural = "Декоративный крепеж"


class Pool(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = '"Бассейн" частный проект. Описание производства и монтажа'
        verbose_name_plural = '"Бассейн" частный проект. Описание производства и монтажа'


class Benches_and_gazebos(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = 'Скамейки и беседки'
        verbose_name_plural = 'Скамейки и беседки'


class Non_standard_metal_structures(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    canonical = models.CharField(max_length=255, verbose_name="canonical", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="description", blank=True, null=True)

    title_h1_1 = models.CharField(max_length=250, verbose_name="Заголовок (h1)")
    img_article = models.ImageField(upload_to="static/upload_img/", verbose_name="img")
    alt_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO alt 'img в статье'")
    title_img_article = models.CharField(max_length=250, blank=True, null=True, verbose_name="SEO title 'img в статье'")
    description_1 = tinymce_models.HTMLField(verbose_name="Описание (блок 1)")
    title_h1_2 = models.CharField(max_length=250,
                                  verbose_name="Второй заголовок (h2) на странице для второго блока", blank=True,
                                  null=True)
    description_2 = tinymce_models.HTMLField(verbose_name="Описание (блок 2 напротив img)", blank=True,
                                             null=True)
    description_3 = tinymce_models.HTMLField(verbose_name="Описание (блок 3 под img) ", blank=True, null=True)

    img1 = models.ImageField(upload_to="static/upload_img/", verbose_name="img1 (загружать подряд по две)", blank=True,
                             null=True)
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
        verbose_name = 'Нестандартные металлоконструкции'
        verbose_name_plural = 'Нестандартные металлоконструкции'
############################################

