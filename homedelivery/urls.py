"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = 'homedelivery'
urlpatterns = [

    path("address/", views.address, name='address'),
    path("confirm/", views.confirm, name='confirm'),
    path("submit/", views.submit, name='submit'),
    path("showonmap/", views.showonmap, name='showonmap'),
    path("orderdetails/", views.orderdetails, name="orderdetails"),
    path("paytm/", views.paytm, name="paytm")
]
