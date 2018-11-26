from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import HD_Address
from django.core import serializers
from django.contrib.auth.models import User
from User.models import Order_Food, Order_User
from Manager.models import Available_Towns
from django.contrib.auth.decorators import login_required


@login_required
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


def showonmap(request):
    context = {'location': '102 Matej Enclave Khajpura Bailey Road Patna', }
    # return HttpResponse('Hello')
    # return {
    #    'location':'102 Matej Enclave Khajpura Bailey Road Patna'
    # } 
    return render(request, 'homedelivery/showonmap.html', context)


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


@login_required
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

