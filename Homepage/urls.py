from django.urls import path
from Homepage import views

app_name = "Homepage"
urlpatterns = [
<<<<<<< HEAD
    path("", views.default)
=======
    path("",views.default ,name="home")
>>>>>>> 3999e350df9a12fd32bd715283b7a5ed698e11cb
]
