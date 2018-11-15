from django.urls import path
from Registration import views

urlpatterns = [
    path("",views.default ),
    path('register/',views.register,name='register')
]
