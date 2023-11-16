from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from main.forms import Form
from .models import Production_and_metalworking, Our_workshop, Bar_counters_and_reception, \
    Сanopies_and_canopies, Furniture_and_interior_elements, Entrances_and_doors, \
    Trusses_and_frames, Colums, Perforated_sheet_metal_structures, Decorative_fasteners, Pool, \
    Benches_and_gazebos, Non_standard_metal_structures


class Production_and_metalworkingView(FormMixin, ListView):
    form_class = Form
    model = Production_and_metalworking
    template_name = "main_menu_html/production_and_metalworking.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Our_workshopView(FormMixin, ListView):
    form_class = Form
    model = Our_workshop
    template_name = "main_menu_html/our_workshop.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Bar_counters_and_receptionView(FormMixin, ListView):
    form_class = Form
    model = Bar_counters_and_reception
    template_name = "main_menu_html/bar_counters_and_reception.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Сanopies_and_canopiesView(FormMixin, ListView):
    form_class = Form
    model = Сanopies_and_canopies
    template_name = "main_menu_html/canopies_and_canopies.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Furniture_and_interior_elementsView(FormMixin, ListView):
    form_class = Form
    model = Furniture_and_interior_elements
    template_name = "main_menu_html/furniture_and_interior_elements.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Entrances_and_doorsView(FormMixin, ListView):
    form_class = Form
    model = Entrances_and_doors
    template_name = "main_menu_html/entrances_and_doors.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Trusses_and_framesView(FormMixin, ListView):
    form_class = Form
    model = Trusses_and_frames
    template_name = "main_menu_html/trusses_and_frames.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ColumnsView(FormMixin, ListView):
    form_class = Form
    model = Colums
    template_name = "main_menu_html/columns.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Perforated_sheet_metal_structuresView(FormMixin, ListView):
    form_class = Form
    model = Perforated_sheet_metal_structures
    template_name = "main_menu_html/perforated_sheet_metal_structures.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Decorative_fastenersView(FormMixin, ListView):
    form_class = Form
    model = Decorative_fasteners
    template_name = "main_menu_html/decorative_fasteners.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class PoolView(FormMixin, ListView):
    form_class = Form
    model = Pool
    template_name = "main_menu_html/pool.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Benches_and_gazebosView(FormMixin, ListView):
    form_class = Form
    model = Benches_and_gazebos
    template_name = "main_menu_html/benches_and_gazebos.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Non_standard_metal_structuresView(FormMixin, ListView):
    form_class = Form
    model = Non_standard_metal_structures
    template_name = "main_menu_html/non-standard_metal_structures.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})