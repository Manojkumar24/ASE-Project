<<<<<<< HEAD
from django.shortcuts import render,reverse
from django.http import HttpResponse
from .models import HD_Address
from django.core import serializers
from django.contrib.auth.models import User
from User.models import Order_Food,Order_User


=======
from django.shortcuts import render
from django.http import HttpResponse
from .models import HD_Address, HD_FoodOrder
from django.core import serializers
>>>>>>> 6b8f19b53121b5183e21c8a26ba6e0bed7ef236b
# Create your views here.


def address(request):
    return render(request, 'homedelivery/address.html')


def submit(request):
    # street=request.POST.get('street', False)
    # dNo=request.POST.get('dNo', False)
    # town=request.POST.get('town', False)
    # phone_number=request.POST.get('phone_number', False)
    # tokenId=HD_FoodOrder.objects.filter(tokenId=1)

    if request.user.is_authenticated:
        username = request.user.username
    else:
        return reverse('Registration:register')
    user = User.objects.get(username=username)
    email = user.email
    #x=Order_User.objects.get(mailId=email,status='draft')
    #t = x.TokenId

    street = request.POST['street']
    dNo = request.POST['dNo']
    town = request.POST['town']
    phone_number = request.POST['phone_number']

    hd_address = HD_Address.objects.create(tokenId=Order_User.objects.get(mailId=email, status='draft'),street=street, dNo=dNo, town=town, phone_number=phone_number)

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
<<<<<<< HEAD
def confirm(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return reverse('Registration:register')
    user = User.objects.get(username=username)
    email = user.email
    x=Order_User.objects.get(mailId=email,status='draft')
    x.status='ordered';t=' '
    t = x.TokenId
    x.save()
    print(t+'he')
    s=Order_Food.objects.filter(TokenId=t,Status='dr')
    for j in s:
        print('shersasura')
        j.Status='conf'
        j.save()
    return render(request,'Homepage/Homepage.html')
