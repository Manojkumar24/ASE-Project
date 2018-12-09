from django.shortcuts import render
from Registration.models import UserProfileInfo
from django.contrib.auth.decorators import login_required
#from Registration.views import user_login


# from User.models import Order_Food,Order_User
# Create your views here.


@login_required
def index(request):
    data = UserProfileInfo.objects.all()
    return render(request, 'User/UserAccount.html', {'data': data})
    User = request.get(user)
    details = UserProfileInfo.objects.filter(user=User)
    return HttpResponse(details)


'''def history(request):
    username = request.POST.get('user')
    user = 
'''
