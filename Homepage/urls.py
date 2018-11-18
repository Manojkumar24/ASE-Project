from django.urls import path
from Homepage import views

app_name = "Homepage"
urlpatterns = [
<<<<<<< HEAD
    path("",views.default ,name="home")
=======
    path("", views.default, name="home")
>>>>>>> 80590861a2232e7441610c2c7f35d8820c68a312
]
