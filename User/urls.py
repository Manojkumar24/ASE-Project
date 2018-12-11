from django.urls import path
from User import views

app_name = 'UserProfile'
urlpatterns = [
    # path('User', views.validate, name='validate'),
    path('user_account/<str:pk>', views.index, name='home'),
    # path("proProvide/<str:pk>", views.proProvide, name='proProvide'),
    # path('hist/<str:name>', views.history, name="Home")
    path("user/confirmed Delivery/<str:token_id>", views.CompletedOrders, name='ConfirmOrder'),
    path("user/cancelled/<str:token_id>", views.CancelOrders, name='CancelOrder')
]
