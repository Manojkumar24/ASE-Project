<<<<<<< HEAD
from django.shortcuts import render, reverse
=======

from django.shortcuts import render,reverse
>>>>>>> 9bf36a9aa4fb910d284e11d1225e627e2774a9b1
from django.http import HttpResponse
from .models import HD_Address
from django.core import serializers
from django.contrib.auth.models import User
<<<<<<< HEAD
from User.models import Order_Food, Order_User
from Manager.models import Available_Towns
from django.contrib.auth.decorators import login_required


@login_required
=======
from User.models import Order_Food,Order_User


>>>>>>> 9bf36a9aa4fb910d284e11d1225e627e2774a9b1
def address(request):
    context = {
        "Towns": []
    }
    for object in Available_Towns.objects.all().values():
        context["Towns"].append(object["Towns"])
    print(context)
    return render(request, 'homedelivery/address.html', context=context)


@login_required
def submit(request):
    username = request.user.username
    user = User.objects.get(username=username)
    email = user.email
<<<<<<< HEAD
    street = request.POST['street']
    dNo = request.POST['dNo']
    town = request.POST['town']
    phone_number = request.POST['phone_number']
    tokenId = Order_User.objects.get(mailId=email, status='draft')
    hd_address = HD_Address.objects.create(
        tokenId=tokenId, street=street, dNo=dNo, town=town, phone_number=phone_number)
    # Changing the tokenid object to the value of the specific tokenid of that object
    tokenId = tokenId.TokenId
    amount = 0
    customer_food = Order_Food.objects.filter(Status='dr', TokenId=tokenId)
    for items in customer_food:
        amount = amount + items.price
    context = {'customer_food': customer_food, 'amount': amount,
               'username': username, 'token': tokenId, 'address': hd_address}
    return render(request, 'homedelivery/shownew.html', context=context)
=======
    #x=Order_User.objects.get(mailId=email,status='draft')
    #t = x.TokenId
    if request.method=='POST':
        street = request.POST['street']
        dNo = request.POST['dNo']
        town = request.POST['town']
        phone_number = request.POST['phone_number']
        temp =Order_User.objects.get(mailId=email, status='draft')
        hd_address = HD_Address.objects.create(tokenId=temp,street=street, dNo=dNo, town=town, phone_number=phone_number)

    if request.user.is_authenticated:
        username = request.user.username
    else:
        return reverse('Registration:register')
    user = User.objects.get(username=username)
    email = user.email
    b = Order_User.objects.get(mailId=email, status='draft');
    t = b.TokenId
    l = 0
    g = Order_Food.objects.filter(Status='dr', TokenId=t)
    for h in g:
        l = l + h.price
    if request.user.is_authenticated:
        Username = request.user.username

        y = {'customer_food': g, 'l': l, 'u': username, 'token': t,'ad':hd_address}

        return render(request, 'homedelivery/shownew.html', context=y)


    hd_address = HD_Address.objects.create(tokenId=HD_FoodOrder.objects.get(
        tokenId=1), street=street, dNo=dNo, town=town, phone_number=phone_number)

    return HttpResponse('Saved')
>>>>>>> 9bf36a9aa4fb910d284e11d1225e627e2774a9b1


def showonmap(request):
    context = {'location': '102 Matej Enclave Khajpura Bailey Road Patna', }
    # return HttpResponse('Hello')
    # return {
    #    'location':'102 Matej Enclave Khajpura Bailey Road Patna'
<<<<<<< HEAD
    # } 
    return render(request, 'homedelivery/showonmap.html', context)
=======
    # }
    return render(request, 'homedelivery/shownew.html', context)
>>>>>>> 9bf36a9aa4fb910d284e11d1225e627e2774a9b1


def orderdetails(request):
    id = 2
    # empty dictionary for storing the models data
    # context = {
    #    'HD_FoodOrder': HD_FoodOrder.objects.get(tokenId=id),
    #    'HD_Address': HD_Address.objects.get(tokenId=id),
    # }
    # lis = []
    # for i in HD_FoodOrder.objects.filter(tokenId=2):
    #    lis.append(str(i))
    context = {
        "HD_FoodOrder": HD_FoodOrder.objects.filter(tokenId=id).values(),
        "HD_Address": HD_Address.objects.filter(tokenId=id).values()
    }
    # return HttpResponse()
    return render(request, 'homedelivery/orderdetails.html', context)
<<<<<<< HEAD


@login_required
=======
>>>>>>> 9bf36a9aa4fb910d284e11d1225e627e2774a9b1
def confirm(request):
    username = request.user.username
    user = User.objects.get(username=username)
    email = user.email
    current_user = Order_User.objects.get(mailId=email, status='draft')
    current_user.status = 'ordered'
    TokenId = current_user.TokenId
    current_user.save()
    current_order = Order_Food.objects.filter(TokenId=TokenId, Status='dr')
    for food_items in current_order:
        food_items.Status = 'conf'
        food_items.save()
    return render(request, 'Homepage/Homepage.html')

