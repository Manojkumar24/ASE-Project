from django.urls import path
from . import views
urlpatterns = [

path('',views.users,name='basic'),

path('statistics/',views.users1,name='statistics'),

path('analysis/',views.users2,name='analysis'),
]
