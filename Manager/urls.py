from django.urls import path, include
from Manager import views

app_name = 'Manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('food_home/', views.food_home, name='food_home'),
    path('tables_home/', views.tables_home, name='tables_home'),
    path('add_food/', views.add_food, name='add_food'),
    path('remove_food/', views.remove_food, name='remove_food'),
    path('add_tables/', views.add_tables, name='add_tables'),
    path('remove_tables/', views.remove_tables, name='remove_tables'),
    path('update_food/<int:f_id>', views.update_food, name='update_food'),
    path('check_update_food/', views.check_update_food, name='check_update_food'),
    path('town_home/', views.town_home, name='town_home'),
    path('add_towns/', views.add_towns, name='add_towns'),
    path('remove_towns/', views.remove_towns, name='remove_towns'),
    path('update_table/<int:id>', views.update_table, name='update_table'),
    path('check_update_table/', views.check_update_table, name='check_update_table'),
    path('history/', include('history.urls')),
    path('list_items/<str:id>', views.list_items, name='list_items'),
    path('send_email/<str:t_id>', views.send_email, name='send_email'),
    path('change_status/<str:f_id>', views.change_status, name='change_status'),
    path('send_com_email/<str:t_id>', views.send_com_email, name='send_com_email'),
    path('send_home_email/<str:t_id>', views.send_home_email, name='send_home_email'),
    path('images_home', views.image_home, name='images_home'),
    path('add_image/', views.add_image, name='add_image'),
    path('remove_image/', views.remove_image, name='remove_image'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('remove_staff/', views.remove_staff, name='remove_staff'),
]
