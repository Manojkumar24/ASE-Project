from django.urls import path
from Homepage import views
from django.views.generic import TemplateView

app_name = "Homepage"
urlpatterns = [
    path("", views.default, name="home"),
    path("searchdb", views.search, name='search'),


]
