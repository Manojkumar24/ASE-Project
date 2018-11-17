from django.shortcuts import render
from django.http import HttpResponse
from .models import HD_Address, HD_FoodOrder 
# Create your views here.
def address(request):
    return render(request, 'homedelivery/address.html')

def submit(request):
    #street=request.POST.get('street', False)
    #dNo=request.POST.get('dNo', False)
    #town=request.POST.get('town', False)
    #phone_number=request.POST.get('phone_number', False)
    #tokenId=HD_FoodOrder.objects.filter(tokenId=1)
    street = request.POST['street']
    dNo=request.POST['dNo']
    town=request.POST['town']
    phone_number=request.POST['phone_number']
    hd_address = HD_Address.objects.create(tokenId=HD_FoodOrder.objects.get(tokenId=2), street=street, dNo=dNo, town=town, phone_number=phone_number)
    return HttpResponse('Saved')