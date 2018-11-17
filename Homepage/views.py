from django.shortcuts import render
from Manager.models import Food_items


def default(request):
    food = Food_items.objects.all()
    contents = {'food': food}
    return render(request, 'Homepage/Homepage.html', contents)
