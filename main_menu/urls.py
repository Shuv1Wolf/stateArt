from django.urls import path

from main_menu.views import Production_and_metalworkingView, Our_workshopView, Bar_counters_and_receptionView, \
    Сanopies_and_canopiesView, Furniture_and_interior_elementsView, Entrances_and_doorsView, Trusses_and_framesView, \
    ColumnsView, Perforated_sheet_metal_structuresView, Decorative_fastenersView, PoolView, Benches_and_gazebosView, \
    Non_standard_metal_structuresView


urlpatterns = [
    path('produce/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    path('244/', Our_workshopView.as_view(), name='our_workshop'),
    path('barnie-stoyki/', Bar_counters_and_receptionView.as_view(), name='bar_counters_and_reception'),
    path('naves/', Сanopies_and_canopiesView.as_view(), name='canopies_and_canopies'),
    path('mebel/', Furniture_and_interior_elementsView.as_view(), name='furniture_and_interior_elements'),
    path('vhodi-dveri/', Entrances_and_doorsView.as_view(), name='entrances_and_doors'),
    path('karkas/', Trusses_and_framesView.as_view(), name='trusses_and_frames'),
    path('kolonni/', ColumnsView.as_view(), name='columns'),
    path('261/', Perforated_sheet_metal_structuresView.as_view(), name='perforated_sheet_metal_structures'),
    path('231/', Decorative_fastenersView.as_view(), name='decorative_fasteners'),
    path('215/', PoolView.as_view(), name='pool'),
    path('280/', Benches_and_gazebosView.as_view(), name='benches_and_gazebos'),
    path('nestandartniye-metallokonstrukcii/', Non_standard_metal_structuresView.as_view(), name='non-standard_metal_structures'),
#
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),
    # path('production_and_metalworking/', Production_and_metalworkingView.as_view(), name='production_and_metalworking'),

]