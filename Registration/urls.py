from django.urls import path
from Registration import views

app_name = 'Registration'
urlpatterns = [
    path("", views.default),
    path('register/', views.register, name='register'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('index/', views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('updateprofile/', views.updateprofile, name="updateprofile")
]
