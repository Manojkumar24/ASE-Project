from django.shortcuts import render
from Registration.models import UserProfileInfo
from django.contrib.auth.decorators import login_required


# from User.models import Order_Food,Order_User
# Create your views here.


@login_required
def index(request):
    data = UserProfileInfo.objects.all()
    return render(request, 'User/UserAccount.html', {'data': data})
