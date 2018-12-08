# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from Manager.models import Food_items
from Registration.models import UserProfileInfo, Staffdetails
from Registration.views import *


# , Staff
# from User.models import Order_Food, Order_User
# from django.contrib.auth.models import User


# def populateOrder_Food():
def default(request):
    if 'breakfast' in request.GET:
        food = Food_items.objects.filter(Category='Tiffin')
    elif 'snack' in request.GET:
        food = Food_items.objects.filter(Category='Snack')
    elif 'starter' in request.GET:
        food = Food_items.objects.filter(Category='Starter')
    else:
        food = Food_items.objects.all()

    if 'employee_id' in request.session:
        staff = request.session.get('employee_id')
        user = Staffdetails.objects.filter(employee_id=staff)
        contents = {'food': food, 'user': user}
        return render(request, 'Homepage/category.html', contents)
    else:
        contents = {'food': food}
        return render(request, 'Homepage/category.html', contents)


def search(request):
    template_name = 'Homepage/search.html'
    query = request.POST.get('FoodRequest')
    if query:
        results = Food_items.objects.filter(Food_Name=query).distinct()
    else:
        results = []
    return render(
        request, template_name, {'results': results})



    #return HttpResponse(details)
