from django.urls import path
from .views import HomePageView, ArticleView, ArticleDetailView, ReviewsView, ContactView, ProjectView, ProjectDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("poleznye-stati/", ArticleView.as_view(), name="poleznye-stati"),
    path("poleznye-stati/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("reviews/", ReviewsView.as_view(), name="reviews"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("project/", ProjectView.as_view(), name="project"),
    path("project/<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
]