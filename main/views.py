from django.views.generic import ListView, DetailView
from django.shortcuts import render
from main.models import Article, News, Reviews

# Create your views here.

class HomePageView(ListView):
    model = News
    template_name = "index.html"
    context_object_name = "news"

class ArticleView(ListView):
    model = Article
    template_name = "article.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = 'object'

class ReviewsView(ListView):
    model = Reviews
    template_name = "reviews.html"
    context_object_name = "reviews"




