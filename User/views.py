from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from Registration.models import UserProfileInfo
from django.contrib.auth.decorators import login_required
# from Registration.views import user_login
from User.models import Order_Food, Order_User


# Create your views here.


def index(request, name=None):
    data = UserProfileInfo.objects.filter(user=name)
    return render(request, 'User/UserAccount.html', {'data': data})


def Order_history(email):
    ordered = Order_User.objects.filter(mailId=email, status='ordered')
    order = {}
    for m in ordered:
        order[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)
    print(order)
    # confirmed_orders = Order_User.objects.filter(mailId=email,status='conf')
    # food_ordered = .values('FoodId', 'quantity', 'time', 'date')
    return order


def PopularFood():
    orders = Order_Food.objects.all()
    print(orders)


def CompletedOrders(request, TokenId):
    ordered = Order_User.objects.get(TokenId=TokenId)
    ordered.status.set('complete')
    return render(request, 'User/UserAccount.html')


@login_required
def proProvide(request, pk=None):
    user = User.objects.get(username=pk)
    email = user.email
    user_order_history = Order_history(email)
    # popular=PopularFood()
    return render(request, "User/UserAccount.html", {'details': user, 'history': user_order_history})

# def cancel(request)
