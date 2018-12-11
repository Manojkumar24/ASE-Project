from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from Manager.models import Food_items
from Registration.models import UserProfileInfo
from django.contrib.auth.decorators import login_required
# from Registration.views import user_login
from User.models import Order_Food, Order_User


# Create your views here.
from eat_at_canteen.models import item_review


@login_required
def index(request, pk=None):
    user = User.objects.get(username=pk)
    email = user.email
    user_order_inOrderd, user_order_inPreparation, user_order_inDelivery = Order_history(email)
    # popular=PopularFood()
    return render(request, "User/UserAccount.html", {'details': user, 'historyDelivery': user_order_inDelivery, 'historyOrdered': user_order_inOrderd, 'historyPreparation': user_order_inPreparation})


def Order_history(email):
    orders_Delivery = {}
    orders_Ordered = {}
    orders_preparation = {}
    orders_delivered = {}

    orders_inDelivery = Order_User.objects.filter(mailId=email, status='in Delivery')
    for m in orders_inDelivery:
        orders_Delivery[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)

    orders_inOrdered = Order_User.objects.filter(mailId=email, status='ordered')
    for m in orders_inOrdered:
        orders_Ordered[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)

    orders_inPreparation = Order_User.objects.filter(mailId=email, status='in Preparation')
    for m in orders_inPreparation:
        orders_preparation[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)

    orders_Delivered = Order_User.objects.filter(status='Completed', mailId=email)
    for m in orders_Delivered:
        orders_delivered[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)

    return orders_Ordered, orders_preparation, orders_Delivery


def PopularFood():
    FoodItems = Food_items.objects.all()
    reviews = item_review.objects.all()
    #print(orders)


def CompletedOrders(request, token_id):
    ordered = Order_User.objects.get(TokenId=token_id)
    ordered.status = 'User Conform'
    ordered.save()
    print(ordered.status)
    username = User.objects.get(email=ordered.mailId)
    return index(request, username)


# def proProvide(request, pk=None):


def CancelOrders(request, token_id):
    ordered = Order_User.objects.get(TokenId=token_id)
    ordered.status = 'cancelled'
    ordered.save()
    print(ordered.status)
    username = User.objects.get(email=ordered.mailId)
    return index(request, username)


def validate(request):
    # if user.is_authentictaed
    return None
