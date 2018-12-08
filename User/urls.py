from django.urls import path
from User import views

app_name = 'User'
urlpatterns = [
    path('', views.index, name="home"),
    path("Prof/<str:name>", views.proProvide, name='proProvide'),
    # path('hist/<str:id>', views.history, name="Home")
]
