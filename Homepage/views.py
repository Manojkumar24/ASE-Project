from django.shortcuts import render
from Manager.models import Food_items
from User.models import Order_Food,Order_User
from django.contrib.auth.models import User



def default(request):
    food = Food_items.objects.all()
    contents = {'food': food}
    return render(request, 'Homepage/Homepage.html', contents)
