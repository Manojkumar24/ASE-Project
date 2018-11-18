from django.shortcuts import render
from Manager.models import Food_items
from User.models import Order_Food,Order_User
from django.contrib.auth.models import User



def default(request):
    food = Food_items.objects.all()
    FoodList = Order_Food.objects.all()
    CustomerFoodList = Order_User.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return reverse('Registration:register')
    user = User.objects.get(username=username)
    email = user.email
    print(email)
    j = 0;
    token = ' '
    for i in CustomerFoodList:
        if i.mailId == email and i.status == 'draft':
            j = 1;
            token = i.TokenId
            print('hiisdfsf');
            print(token)
            break
    if j == 1:
        g = Order_Food.objects.filter(Status='dr', TokenId=token)
    else:
        g=None
    contents = {'food': food,'g':g}
    return render(request, 'Homepage/Homepage.html', contents)
