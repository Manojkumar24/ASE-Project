from django.conf.urls import url
from django.urls import path
from Registration import views

app_name = 'Registration'
urlpatterns = [
    path("", views.default),
    path('register/', views.register, name='register'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('index/', views.index, name='index'),
    path('staff_registration/', views.staff_registration, name='staff_registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('staff_logout/', views.staff_logout, name='staff_logout'),
    # url(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    path('activate_account/<uidb64>/<token>/', views.activate_account, name='activate_account'),
    # profile_edits
    path('editprofile/', views.editprofile, name='editprofile'),
    path('updateprofile/', views.updateprofile, name="updateprofile"),

]
