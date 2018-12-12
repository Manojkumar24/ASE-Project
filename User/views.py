from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from collections import OrderedDict
from Manager.models import Food_items
from Registration.models import UserProfileInfo
from django.contrib.auth.decorators import login_required
# from Registration.views import user_login
from User.models import Order_Food, Order_User
import datetime
from eat_at_canteen.models import item_review


def index(request, pk=None):
    user = User.objects.get(username=pk)
    email = user.email
    user_order_inOrderd, user_order_inPreparation, user_order_inDelivery, orders_deliverd, cancel = Order_history(email,
                                                                                                                  True)
    popular = PopularFood()
    print(popular)
    return render(request, "User/UserAccount.html",
                  {'details': user, 'historyDelivery': user_order_inDelivery, 'historyOrdered': user_order_inOrderd,
                   'historyPreparation': user_order_inPreparation, 'orders_delivered': orders_deliverd,
                   'popular': popular, 'cancel': cancel})  #


def Order_history(email, cancelState):
    orders_Delivery = {}
    orders_Ordered = {}
    orders_preparation = {}
    orders_delivered = {}
    cancel = {}
    orders_inDelivery = Order_User.objects.filter(mailId=email, status='in Delivery')
    for m in orders_inDelivery:
        orders_Delivery[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)

    orders_inOrdered = Order_User.objects.filter(mailId=email, status='ordered')
    for m in orders_inOrdered:
        orders_Ordered[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)
        if cancelState:
            cancel[m.TokenId] = True
        else:
            cancel[m.TokenId] = False

    orders_inPreparation = Order_User.objects.filter(mailId=email, status='in Preparation')
    for m in orders_inPreparation:
        orders_preparation[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)

    orders_Delivered = Order_User.objects.filter(status='Completed', mailId=email)
    for m in orders_Delivered:
        orders_delivered[m.TokenId] = Order_Food.objects.filter(Status='conf', TokenId=m.TokenId)

    return orders_Ordered, orders_preparation, orders_Delivery, orders_delivered, cancel


def PopularFood():
    FoodItems = Food_items.objects.all()
    sort_food = {}
    ratings = {}
    k = 0
    for m in FoodItems:
        n = item_review.objects.filter(product__Food_id=m.Food_id)
        item_count = item_review.objects.filter(product__Food_id=m.Food_id).count() + 1

        for l in n:
            if l.rating:
                k = k + l.rating
            else:
                k = m.rating
                item_count = 1
        ratings[m.Food_id] = k / item_count
        m.rating = k / item_count
        m.save()
    food_sortBy_Rating = sorted(ratings.items())
    print('adsda', ratings)
    print(food_sortBy_Rating)
    # foodId = []
    for k in food_sortBy_Rating:
        sort_food[k[0]] = Food_items.objects.filter(Food_id=k[0])
    # print(sort_food)
    return sort_food


def CompletedOrders(request, token_id):
    ordered = Order_User.objects.get(TokenId=token_id)
    ordered.status = 'User Conform'
    ordered.save()
    print(ordered.status)
    username = User.objects.get(email=ordered.mailId)
    return index(request, username)


# def proProvide(request, pk=None):


def CancelOrders(request, token_id):
    print('sadsdas')
    ordered = Order_User.objects.get(TokenId=token_id)
    print('asdasdasd')
    email = ordered.mailId
    order = Order_Food.objects.get(TokenId=token_id)
    if order.date == datetime.datetime.date and order.time - datetime.datetime.time == 30:
        ordered.status = 'cancelled'
        ordered.save()
        print(ordered.status)
        username = User.objects.get(email=email)
        return index(request, username)

    else:
        return Order_history(email, False)
