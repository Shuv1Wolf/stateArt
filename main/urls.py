from django.urls import path
from .views import HomePageView, ArticleView, ArticleDetailView, ReviewsView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("poleznye-stati/", ArticleView.as_view(), name="poleznye-stati"),
    path("poleznye-stati/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("reviews/", ReviewsView.as_view(), name="reviews"),
]