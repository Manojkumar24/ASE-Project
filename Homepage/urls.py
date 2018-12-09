from django.urls import path
from Homepage import views

app_name = "Homepage"
urlpatterns = [
    path("", views.default, name="home"),
    path("searchdb", views.search, name='search'),
    #path("Prof", views.proProvide, name='proProvide'),
]
