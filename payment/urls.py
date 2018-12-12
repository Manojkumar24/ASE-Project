from django.contrib import admin
from django.urls import path
from . import views


app_name = 'payment'
urlpatterns = [

    path('pay/', views.pay, name='pay'),
    path('check/', views.check, name='check'),
    path('status/', views.status, name='status'),
]
