from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import HttpResponseRedirect
from django.views.generic.edit import FormMixin
from main.models import Article, News, Reviews, Project,Work_Example
from .forms import Form


class HomePageView(FormMixin, ListView):
    form_class = Form
    model = News
    template_name = "html/index.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['work_example'] = Work_Example.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ArticleView(FormMixin, ListView):
    form_class = Form
    model = Article
    template_name = "html/article.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ArticleDetailView(FormMixin, DetailView):
    form_class = Form
    model = Article
    template_name = "html/article_detail.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})

class ReviewsView(FormMixin, ListView):
    form_class = Form
    model = Reviews
    template_name = "html/reviews.html"
    context_object_name = "reviews"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ContactView(FormMixin, TemplateView):
    template_name = "html/contacts.html"
    form_class = Form

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ProjectView(FormMixin, ListView):
    form_class = Form
    model = Project
    template_name = "html/project.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ProjectDetailView(FormMixin, DetailView):
    form_class = Form
    model = Project
    template_name = "html/project_detail.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Work_ExampleDetailView(FormMixin, DetailView):
    form_class = Form
    model = Work_Example
    template_name = "html/work_example.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})
