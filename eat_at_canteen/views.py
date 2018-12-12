from django.shortcuts import render, redirect, reverse
# Create your views here.
from django.contrib.auth.models import User

from Manager.models import Food_items, Dining_Tables
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from User.models import Order_Food, Order_User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from .models import user_review, Review
from .forms import ReviewForm
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from .serializers import reviewserializer
from rest_framework.response import Response
from rest_framework import status
import random


def index(request):
    return render(request, 'eat_at_canteen/index.html')


class ReviewView(APIView):
    def get(self, request):
        reviewlogs = Review.objects.all()
        serializer = reviewserializer(reviewlogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = reviewserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#@login_required
def table(request):
    t = Dining_Tables.objects.all()

    t_dict = {'t': t}
    return render(request, 'eat_at_canteen/BOOKTABLE.html', context=t_dict)


#@login_required
def check(request):
    if request.method == 'POST':
        t = Dining_Tables.objects.all();
        if 'username' in request.session:
            username = request.session['username']
        else:
            return reverse('Registration:register')
        user = User.objects.get(username=username)
        email = user.email
        b = Order_User.objects.get(mailId=email, status='draft');
        a = b.TokenId
        g = Order_Food.objects.filter(Status='dr', TokenId=a)

        table = " "
        for u in t:

            if str(u.Table_id) in request.POST:
                print('hiiuuh')
                print('jii')
                u.availability = False
                u.save()
                if table == " ":
                    table = str(u.Table_id)
                else:
                    table = table + ',' + str(u.Table_id)
                print(table)
                for h in g:
                    h.TableId = table
                    print(h.TableId)
                    h.save()

        l = 0
        for h in g:
            l = l + h.price

        x = {'customer_food': g, 'table': table, 'l': l, 'u': username, 'token': a}
        return render(request, 'eat_at_canteen/show.html', context=x)


#@login_required
def checkout(request):
    print('hii')
    if 'username' in request.session:
        username = request.session['username']
    else:
        return reverse('Registration:register')
    user = User.objects.get(username=username)
    email = user.email
    b = Order_User.objects.get(mailId=email, status='draft');
    a = b.TokenId
    g = Order_Food.objects.filter(Status='dr', TokenId=a)
    l = 0
    for h in g:
        l = l + h.price
    b.totalPrice = float(l)
    b.save()
    x = {'customer_food': g, 'l': l, 'u': username, 'token': a}
    return render(request, 'eat_at_canteen/show.html', context=x)


#@login_required
def order(request, pk=None):
    if request.method == 'POST':
        FoodList = Order_Food.objects.all()
        CustomerFoodList = Order_User.objects.all()

        Food = request.POST.get('food')
        print(Food)
        Price = request.POST.get('price')
        print(Food, Price)
        print('added1')

        if 'username' in request.session:
            username = request.session['username']
        else:
            return reverse('Registration:register')
        user = User.objects.get(username=username)
        email = user.email
        print(email)
        j = 0
        for i in CustomerFoodList:
            if i.mailId == email and i.status == 'draft':
                print('fgdfgdgdgdg')
                j = 1
                break
        print(j)

        if j == 0:
            def uniqueid():
                seed = random.getrandbits(32)
                while True:
                    yield seed
                    seed += 1

            unique_sequence = uniqueid()
            id1 = next(unique_sequence)
            a = Order_User()
            a.mailId = email
            a.TokenId = id1

            f = Food_items.objects.get(Food_Name=Food)
            c = Order_Food.objects.create(FoodId=f, price=Price, quantity=1, date=datetime.date.today(),
                                          time=datetime.datetime.now(), TableId=0, TokenId=a.TokenId)
            a.totalPrice = Price
            a.save()
            c.save()


        else:
            a = Order_User.objects.get(mailId=email, status='draft')
            d = a.TokenId
            print(d)
            f = Food_items.objects.get(Food_Name=Food)
            print(f.Food_Price)
            l = 0

            for u in FoodList:
                if u.FoodId == f and u.TokenId == d:
                    u.quantity = u.quantity + 1
                    l = 1
                    u.price = u.quantity * float(Price)
                    a.totalPrice = a.totalPrice
                    u.save()
                    print('hifsdfsi')
                    break
            if l == 0:
                c = Order_Food.objects.create(FoodId=f, price=Price, quantity=1, date=datetime.date.today(),
                                              time=datetime.datetime.now(), TableId=0, TokenId=a.TokenId)
                a.totalPrice = a.totalPrice + float(Price)
                a.save()
                c.save()

        return reverse('Homepage:home')
    elif request.method == 'GET':
        FoodList = Order_Food.objects.all()
        CustomerFoodList = Order_User.objects.all()
        w = Food_items.objects.get(Food_id=pk)
        Food = w.Food_Name
        print(Food)
        Price = w.Food_Price
        print(Food, Price)
        print('added1')

        if 'username' in request.session:
            username = request.session['username']
        else:
            return reverse('Registration:register')
        user = User.objects.get(username=username)
        email = user.email
        print(email)
        j = 0
        for i in CustomerFoodList:
            if i.mailId == email and i.status == 'draft':
                print('fgdfgdgdgdg')
                j = 1
                break
        print(j)

        if j == 0:
            def uniqueid():
                seed = random.getrandbits(32)
                while True:
                    yield seed
                    seed += 1

            unique_sequence = uniqueid()
            id1 = next(unique_sequence)
            a = Order_User()
            a.mailId = email
            a.TokenId = id1

            f = Food_items.objects.get(Food_Name=Food)
            c = Order_Food.objects.create(FoodId=f, price=Price, quantity=1, date=datetime.date.today(),
                                          time=datetime.datetime.now(), TableId=0, TokenId=a.TokenId)
            a.totalPrice = Price
            a.save()
            c.save()


        else:
            a = Order_User.objects.get(mailId=email, status='draft')
            d = a.TokenId
            print(d)
            f = Food_items.objects.get(Food_Name=Food)
            print(f.Food_Price)
            l = 0

            for u in FoodList:
                if u.FoodId == f and u.TokenId == d:
                    u.quantity = u.quantity + 1
                    l = 1
                    u.price = u.quantity * float(Price)
                    a.totalPrice = a.totalPrice
                    u.save()
                    print('hifsdfsi')
                    break
            if l == 0:
                c = Order_Food.objects.create(FoodId=f, price=Price, quantity=1, date=datetime.date.today(),
                                              time=datetime.datetime.now(), TableId=0, TokenId=a.TokenId)
                a.totalPrice = a.totalPrice + float(Price)
                a.save()
                c.save()
        reverse('Homepage:Home')


# @login_required()
def cart(request, username):
    FoodList = Order_Food.objects.all()
    CustomerFoodList = Order_User.objects.all()
    try:
        user = User.objects.get(username=username)
    except:
        return  redirect('Homepage:home')
    email = user.email
    print(email)
    j = 0
    token = ' '
    for i in CustomerFoodList:
        if i.mailId == email and i.status == 'draft':
            j = 1
            token = i.TokenId
            print('hiisdfsf')
            print(token)
            break
    if j == 1:
        g = Order_Food.objects.filter(Status='dr', TokenId=token)
        l = 0
        for h in g:
            l = l + h.price
    else:
        g = None
        l = None

    x = {'items': g, 'l': l, 'username': username}
    return render(request, 'eat_at_canteen/cart.html', context=x)


#@login_required
def Delete(request):
    a = request.POST.get('food')
    f = Food_items.objects.get(Food_Name=a)

    if 'username' in request.session:
        username = request.session['username']
    else:
        return reverse('Registration:register')
    user = User.objects.get(username=username)
    email = user.email
    x = Order_User.objects.get(mailId=email, status='draft')
    t = x.TokenId
    s = Order_Food.objects.get(TokenId=t, FoodId=f)

    print(s)
    s.delete()
    return redirect('eat_at_canteen:cart')


#@login_required
def confirm(request):
    if 'username' in request.session:
        username = request.session['username']
    else:
        return reverse('Registration:register')
    user = User.objects.get(username=username)
    email = user.email
    x = Order_User.objects.get(mailId=email, status='draft')
    x.status = 'ordered'
    t = x.TokenId
    x.save()
    print(t + 'he')
    s = Order_Food.objects.filter(TokenId=t, Status='dr')
    l = Food_items.objects.all()
    for j in s:
        c = Food_items.objects.get(Food_Name=j.FoodId)
        c.quantity = c.quantity - j.quantity
        c.save()
        print('shersasura')
        j.Status = 'conf'
        j.save()
    return redirect('Homepage:home', category='all')


#@login_required
def update(request):
    print('came to update top part')
    if request.method == 'POST':
        print()
        food = Order_Food.objects.get(id=(request.POST["id"]))
        price = float(request.POST['price'])
        quantity = int(request.POST['quantity'])
        food.price = price
        food.quantity = quantity
        food.save()
        print(food)
        print('came to update')
        return HttpResponse('hi')


def review(request):
    username = request.user.username
    latest_review_list = user_review.objects.order_by('latest_pub_date')
    form = ReviewForm()
    x = {'form': form, 'latest_review_list': latest_review_list, 'username': username}
    return render(request, 'eat_at_canteen/review.html', context=x)


#@login_required
def add_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user.username
        review = Review()
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        p = 0
        w = user_review.objects.all()
        print(user_name)
        for i in w:
            if i.user_name == user_name:
                p = 1
                a = user_review.objects.get(user_name=user_name)
                a.latest_review = comment;
                a.latest_pub_date = datetime.datetime.now();
                a.average_rating = ((a.average_rating * a.No_Reviews) + rating) / (a.No_Reviews + 1);
                a.No_Reviews = a.No_Reviews + 1
                a.save()
        if p == 0:
            a = user_review.objects.create(user_name=user_name, latest_review=comment,
                                           latest_pub_date=datetime.datetime.now(), No_Reviews=1, average_rating=rating)
            a.save()

        return HttpResponseRedirect(reverse('eat_at_canteen:hotel_review'))

    return render(request, 'eat_at_canteen/review.html', {'form': form})
