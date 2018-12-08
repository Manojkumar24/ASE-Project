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


'''def history(request, email):
    user_orders = Order_User.objects.filter(mailId=email)
    
    return '''



def proProvide(request, pk=None):
    user = User.objects.get(username=pk)
    return render(request, "User/UserAccount.html", {'details': user})

# def cancel(request)
