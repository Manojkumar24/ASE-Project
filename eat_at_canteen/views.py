from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm
from .models import FoodItems,CustomerFoodItems,Tables
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.utils import timezone



from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


import random
def index(request):
    return render(request,'eat_at_canteen/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in ,Nice!")

def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'eat_at_canteen/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'eat_at_canteen/login.html',{})


@login_required
def order(request):
    if(request.method=='POST'):
        FoodList = FoodItems.objects.order_by('Price')
        CustomerFoodList = CustomerFoodItems.objects.all()
        Food = request.POST.get('food')
        Price = request.POST.get('price')
        Quantity = request.POST.get('Quantity')
        print(Food, Price, Quantity)
        print('added1')
        l=0
        for u in CustomerFoodList:
           if u.Foodname==Food:
               u.Quantity=u.Quantity+int(Quantity)
               l=1
               u.Price=u.Quantity*float(Price)
               u.save()
               break
        if l==0:
            a=CustomerFoodItems()
            a.Foodname=Food
            a.Price=float(Price)
            a.Quantity =int(Quantity)
            a.save()
        CustomerFoodList = CustomerFoodItems.objects.all()
        l = 0
        for g in CustomerFoodList:
            l = l + g.Price
        food_dict = {'items': FoodList,'citems': CustomerFoodList,'l':l}

        return render(request, 'eat_at_canteen/order.html', context=food_dict)
    else:
        print('added2')
        FoodList=FoodItems.objects.order_by('Price')
        print('hii')
        print(request.GET.get('f'))
        CustomerFoodList = CustomerFoodItems.objects.all()
        l = 0
        for g in CustomerFoodList:
            l = l + g.Price
        food_dict={'items':FoodList,'citems':CustomerFoodList,'l':l}
        return render(request,'eat_at_canteen/order.html',context=food_dict)

@login_required
def book(request):

    if request.method=='POST':
        t=Tables.objects.all()
        print(t)
        a={};b={};
        for u in t:
            print(u.Table_No)
            print(u.Status)
            c='table'+str(u.Table_No)
            b={c:u}
            a.update(b)

        return render(request, 'eat_at_canteen/BOOKTABLE.html', context=a)
    else:
        t = Tables.objects.all()
        a = {};
        b = {};
        for u in t:
            print(u.Table_No)
            print(u.Status)
            c='table'+str(u.Table_No)
            b={c:u}
            a.update(b)
        print('jii')
        return render(request, 'eat_at_canteen/BOOKTABLE.html', context=a)


@login_required
def check(request):
    t = Tables.objects.all();
    table=''
    for u in t:

        if 'table'+str(u.Table_No) in request.POST:
            u.Status='Reserved'
            if not table:
                table=str(u.Table_No)
            else:
                table=str(table)+','+str(u.Table_No)
            u.save()
    b=CustomerFoodItems.objects.all();l=0
    for g in b:
        l=l+g.Price
    if request.user.is_authenticated:
        Username = request.user.username

    print(table);
    def uniqueid():
        seed = random.getrandbits(32)
        while True:
            yield seed
            seed += 1

    unique_sequence = uniqueid()
    id1 = next(unique_sequence)
    x={'customer_food':b,'table':table,'l':l,'u':Username,'token':id1}


    return render(request,'eat_at_canteen/show.html',context=x)

@login_required
def cart(request):
    b = CustomerFoodItems.objects.all()
    l=0
    for g in b:
        l=l+g.Price


    x={'items':b,'l':l}
    return render(request,'eat_at_canteen/cart.html',context=x)

class AboutView(TemplateView):
    template_name = 'eat_at_canteen/about.html'

def showposts(request):


        q = Post.objects.all()
        p = {'u': q}
        return render(request, 'eat_at_canteen/posts.html', context=p)




def Delete(request):
    a=request.POST.get('food')
    instance = CustomerFoodItems.objects.get(Foodname=a)
    print(instance)
    instance.delete()
    return redirect('eat_at_canteen:ordernew')
