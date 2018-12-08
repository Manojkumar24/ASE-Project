from django.urls import path
from User import views

app_name = 'User'
urlpatterns = [
    path('', views.index, name="home"),
    path("proProvide/<str:pk>", views.proProvide, name='proProvide'),
    #path('hist/<str:name>', views.history, name="Home")
]
