from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register((Food_items, Dining_Tables, Available_Towns, Admin_Image))
