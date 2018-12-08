from django.shortcuts import render
from Registration.forms import UserForm, UserProfileInfoForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfileInfo


def default(request):
    return render(request, 'Registration/Registration_01.html')


def index(request):
    return render(request, 'Registration/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Homepage:home'))


@login_required
def special(request):
    return HttpResponse("You are logged in ,Nice!")


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'Registration/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Homepage:home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'Registration/login.html', {})


@login_required
def editprofile(request):
    updated = False
    user = User.objects.filter(username=request.user)
    # print(user)
    userId = User.objects.get(username=request.user).id
    # user = User.objects.filter(username=request.user)
    userprofileinfo = UserProfileInfo.objects.filter(id=userId)
    context = {
    }
    # print(user.values())
    for field in user.values():
        context["user"] = field
    for field in userprofileinfo.values():
        context["userprofileinfo"] = field
    # print(context)
    return render(request, 'Registration/editprofile.html', context=context)
    # return HttpResponse("user")


@login_required
def updateprofile(request):
    user = User.objects.get(username=request.user)
    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.set_password(request.POST['password'])
    user.save()
    userprofileinfo = UserProfileInfo.objects.get(user=request.user)
    userprofileinfo.address = request.POST['address']
    userprofileinfo.city = request.POST['city']
    userprofileinfo.pincode = request.POST['pincode']
    userprofileinfo.save()
    return HttpResponse("Saved")
