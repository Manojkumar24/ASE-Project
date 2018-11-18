from django.shortcuts import render
from django.http import HttpResponse
from .models import HD_Address, HD_FoodOrder
from django.core import serializers
# Create your views here.


def address(request):
    return render(request, 'homedelivery/address.html')


def submit(request):
    # street=request.POST.get('street', False)
    # dNo=request.POST.get('dNo', False)
    # town=request.POST.get('town', False)
    # phone_number=request.POST.get('phone_number', False)
    # tokenId=HD_FoodOrder.objects.filter(tokenId=1)
    street = request.POST['street']
    dNo = request.POST['dNo']
    town = request.POST['town']
    phone_number = request.POST['phone_number']
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
