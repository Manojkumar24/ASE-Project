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
    url(r'^index/',views.index,name='index'),
    url(r'^register/',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),


    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^special/',views.special,name='special'),

    url(r'^order/',views.order,name='ordernew'),
    url(r'^book/$',views.book,name='Booktable'),
    url(r'^check/', views.check, name='checkout'),
    url(r'^Cart/',views.cart, name='cart'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),

    url(r'^reviews/',views.showposts,name='reviews'),
    url(r'^delete/',views.Delete,name='delete')

]

#added
""" url(r'^$',views.index,name='index'),
    url(r'^basic_app/',include('basic_app.urls')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^special/',views.special,name='special'),

    url(r'^order/',views.order,name='ordernew'),
    url(r'^book/',views.book,name='Booktable'),"""