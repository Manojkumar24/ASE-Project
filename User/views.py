from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from Registration.models import UserProfileInfo
from django.contrib.auth.decorators import login_required
# from Registration.views import user_login


from User.models import Order_Food, Order_User


# Create your views here.


@login_required
def index(request, name=None):
    data = UserProfileInfo.objects.filter(user=name)
    return render(request, 'User/UserAccount.html', {'data': data})


'''
def history(request):
    username = request.user.get('user')
    user = UserProfileInfo.objects.filter()
    
'''


def proProvide(request, name=None):
    # User = request.get(name)
    user = User.objects.filter(username=name)
    #details = Order_User.objects.filter(mailId=user.email)
    # y=typeof(user)
    return HttpResponse(user.email)
    #if details:
     #   return render(request, "User/UserAccount.html", {'details':details})
