from django.shortcuts import render
# Create your views here.
from Manager.models import Food_items,Dining_Tables
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect

from django.utils import timezone
from User.models import Order_Food, Order_User


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
def book(request):
    if (request.method == 'POST'):
        def uniqueid():
            seed = random.getrandbits(32)
            while True:
                yield seed
                seed += 1
        unique_sequence = uniqueid()
        FoodList = Order_Food.objects.all()
        CustomerFoodList = Order_User.objects.all()
        Food = request.POST.get('food')
        Price = request.POST.get('price')
        a = Order_Food()
        a.TokenId = unique_sequence
        a.Quantity = 1
        a.Price=float(Price)
        a.FoodId=12
        print(Food, Price, Quantity)
        print('added1')
        l = 0
        for u in CustomerFoodList:
            if u == Food:
                u.Quantity = u.Quantity + int(Quantity)
                l = 1
                u.Price = u.Quantity * float(Price)
                u.save()
                break
        if l == 0:
            a = CustomerFoodItems()
            a.Foodname = Food
            a.Price = float(Price)
            a.Quantity = int(Quantity)
            a.save()
        CustomerFoodList = CustomerFoodItems.objects.all()
        l = 0
        for g in CustomerFoodList:
            l = l + g.Price
        food_dict = {'items': FoodList, 'citems': CustomerFoodList, 'l': l}

        return render(request, 'eat_at_canteen/order.html', context=food_dict)









