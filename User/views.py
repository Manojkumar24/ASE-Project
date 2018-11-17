from django.shortcuts import render
from .models import Order_Food,Order_User
from Registration.models import UserProfileInfo
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'User/UserAccount.html')


@login_required
def userprofile(request):
    data = UserProfileInfo.objects.all()
    Data = {'data':data}
    return()
@login_required()
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Homepage:home'))