from django.urls import path
from Registration import views

app_name = 'Registration'
urlpatterns = [
    path("",views.default ),
    path('register/',views.register,name='register'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('index/',views.index,name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('staff_registration/',views.staff_registration,name='staff_registration'),
    path('cust_verify/',views.cust_verify,name='cust_verify'),
    path('email_verify',views.email_verify,name='email_verify'),
    path('verified_email/',views.email_verified,name='email_verified')
]
