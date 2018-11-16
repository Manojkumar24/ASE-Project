from django.urls import path
from . import views
urlpatterns = [

path('',views.users,name='canteen-model2'),
#path('model1/',views.chart,name='canteen-model3'),
#path('model1/dummy/',views.dummy,name='canteen-modl4'),
]
