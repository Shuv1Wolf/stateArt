from django.contrib import admin

# Register your models here.

from .models import Production_and_metalworking, Our_workshop, Bar_counters_and_reception, \
    Сanopies_and_canopies, Furniture_and_interior_elements, Entrances_and_doors, \
    Trusses_and_frames, Colums, Perforated_sheet_metal_structures, Decorative_fasteners, Pool, \
    Benches_and_gazebos, Non_standard_metal_structures

admin.site.register(Production_and_metalworking)
admin.site.register(Our_workshop)
admin.site.register(Bar_counters_and_reception)
admin.site.register(Сanopies_and_canopies)
admin.site.register(Furniture_and_interior_elements)
admin.site.register(Entrances_and_doors)
admin.site.register(Trusses_and_frames)
admin.site.register(Colums)
admin.site.register(Perforated_sheet_metal_structures)
admin.site.register(Decorative_fasteners)
admin.site.register(Pool)
admin.site.register(Benches_and_gazebos)
admin.site.register(Non_standard_metal_structures)