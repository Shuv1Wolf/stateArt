from django.contrib import admin

# Register your models here.

from .models import Production_and_metalworking, Our_workshop, Bar_counters_and_reception, \
    Сanopies_and_canopies, Furniture_and_interior_elements, Entrances_and_doors, \
    Trusses_and_frames, Colums, Perforated_sheet_metal_structures, Decorative_fasteners, Pool, \
    Benches_and_gazebos, Non_standard_metal_structures



class Admin(admin.ModelAdmin):
    fieldsets = (
        ('meta', {
            'fields': ('title', 'canonical', 'description'),
        }),
        ('Запись', {
            'fields': ('title_h1_1', 'img_article', 'alt_img_article', 'title_img_article', 'description_1', 'title_h1_2', 'description_2', 'description_3'),
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
admin.site.register(Production_and_metalworking, Admin)


admin.site.register(Our_workshop, Admin)
admin.site.register(Bar_counters_and_reception, Admin)
admin.site.register(Сanopies_and_canopies, Admin)
admin.site.register(Furniture_and_interior_elements, Admin)
admin.site.register(Entrances_and_doors, Admin)
admin.site.register(Trusses_and_frames, Admin)
admin.site.register(Colums, Admin)
admin.site.register(Perforated_sheet_metal_structures, Admin)
admin.site.register(Decorative_fasteners, Admin)
admin.site.register(Pool, Admin)
admin.site.register(Benches_and_gazebos, Admin)
admin.site.register(Non_standard_metal_structures, Admin)