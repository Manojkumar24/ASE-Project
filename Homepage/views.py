from django.shortcuts import render
from Manager.models import Food_items


# from User.models import Order_Food, Order_User
# from django.contrib.auth.models import User
# def populateOrder_Food():

def default(request):
    food = Food_items.objects.all()
    contents = {'food': food}
    return render(request, 'Homepage/Homepage.html', contents)


def search(request):
    template_name = 'Homepage/search.html'

    query = request.GET.get('FoodRequest')
    if query:
        results = Food_items.objects.filter(Food_Name=query).distinct()
    else:
        results = []
    return render(
        request, template_name, {'results': results})
