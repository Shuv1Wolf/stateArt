from django.urls import path
from .views import HomePageView, ArticleView, ArticleDetailView,\
    ReviewsView, ContactView, ProjectView, ProjectDetailView,\
    Work_ExampleDetailView, Work_Example_In_ProjectDetailView,\
    DeliveryView, How_to_offerView


urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("work_example/<slug:slug>/", Work_ExampleDetailView.as_view(), name="work_example"),
    path("poleznye-stati/", ArticleView.as_view(), name="poleznye-stati"),
    path("poleznye-stati/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("reviews/", ReviewsView.as_view(), name="reviews"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("project/", ProjectView.as_view(), name="project"),
    path("project/<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
    path("project/work_example/<slug:slug>/", Work_Example_In_ProjectDetailView.as_view(), name="project_example"),
    path("delivery/", DeliveryView.as_view(), name='delivery'),
    path("offer/", How_to_offerView.as_view(), name='offer'),
]