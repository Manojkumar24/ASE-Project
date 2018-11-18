from django.urls import path
from Homepage import views

app_name = "Homepage"
urlpatterns = [
    path("",views.default ,name="home"),
    path("", views.default, name="home")
]
