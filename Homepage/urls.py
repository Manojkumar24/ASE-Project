<<<<<<< HEAD
from django.urls import path
from Homepage import views

app_name = "Homepage"
urlpatterns = [
    path("",views.default ,name="home")
]
=======
from django.urls import path
from Homepage import views

app_name = "Homepage"
urlpatterns = [
    path("", views.default, name="home"),
    path("searchdb", views.search, name='search'),
]
>>>>>>> 9bf36a9aa4fb910d284e11d1225e627e2774a9b1
