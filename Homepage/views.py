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

<<<<<<< HEAD
    contents = {'food': food}

    if 'employee_id' in request.session:
        staff = request.session['employee_id']
        user = Staffdetails.objects.filter(employee_id=staff)
        content1 = {'user': user}
        return render(request, 'Homepage/Homepage.html', contents, content1)
    else:
        return render(request, 'Homepage/Homepage.html', contents)
=======
    if 'employee_id' in request.session:
        staff = request.session.get('employee_id')
        user = Staffdetails.objects.filter(employee_id=staff)
        contents = {'food': food, 'user': user}
        return render(request, 'Homepage/category.html', contents)
    else:
        contents = {'food': food}
        return render(request, 'Homepage/category.html', contents)
>>>>>>> parent of b8c06fa... Displaying User History


def search(request):
    template_name = 'Homepage/search.html'
    query = request.POST.get('FoodRequest')
    if query:
        results = Food_items.objects.filter(Food_Name=query).distinct()
    else:
        results = []
    return render(
        request, template_name, {'results': results})


