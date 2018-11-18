from django.shortcuts import render
# Create your views here.
from Manager.models import Food_items,Dining_Tables
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect

from django.utils import timezone



from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


import random
def index(request):
    return render(request,'eat_at_canteen/index.html')

def table(request):
    t=Dining_Tables.objects.all()


    t_dict = {'t': t}
    return render(request, 'eat_at_canteen/BOOKTABLE.html', context=t_dict)

def check(request):
    if request.method == 'POST':
        t = Dining_Tables.objects.all();

        table=" "
        for u in t:
            if str(u.Table_id) in request.POST:
                print('jii')
                u.availability = False
                if table==" ":
                    table=str(u.Table_id)
                else:
                    table=table+','+str(u.Table_id)
                u.save()
        return HttpResponse('hii')
    return HttpResponse('hello')

def show(request):
    print('added2')
    FoodList = Food_items.objects.order_by('Food_Price')
    print('hii')
    food_dict = {'items': FoodList}
    return render(request, 'eat_at_canteen/order.html', context=food_dict)









