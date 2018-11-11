"""Canteen_System_Automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
#from Registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', include('Manager.urls')),
    path('canteen/', include('history.urls')),
<<<<<<< HEAD
    path('', include('Homepage.urls')),


    path('registration', include('Registration.urls')),
    #path('ec/',include('eat_at_canteen.urls'))

=======
    path('HomePage/', include('Homepage.urls')),
    path('canteen/',include('history.urls')),
    #path('HomePage/',include('User.urls')),
<<<<<<< HEAD
    path('registration/',include('Registration.urls')),
    #path('ec/',include('eat_at_canteen.urls'))
=======
    path('registration',include('Registration.urls')),
    path('ec/',include('eat_at_canteen.urls'))
>>>>>>> 7ebfe8cc2289f41ebf3612408c614a5aac040dbb
>>>>>>> d72f8044f6e315edcc853a5a2150cf860897a7f8
]
