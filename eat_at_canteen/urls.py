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
from django.conf.urls import url,include
from . import views
app_name='eat_at_canteen'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('check/',views.check,name='check'),
    path('checkout/', views.checkout, name='checkout'),
    path('table/',views.table,name='table'),
    path('orderfood/',views.order,name='order'),
    path('order/<int:pk>/',views.order,name='orderagain'),
    path('cart/',views.cart,name='cart'),
    path('delete/',views.Delete,name='delete'),
    path('confirm/',views.confirm,name='confirm'),
    path('update/',views.update,name='update'),
    path('review/', views.review, name='hotel_review'),
    path('add/', views.add_review, name='add_review'),
    path('re/',views.ReviewView.as_view()),
]

