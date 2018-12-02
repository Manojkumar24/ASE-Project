from django.contrib import messages
from django.shortcuts import render
from Registration.forms import UserForm,UserProfileInfoForm,StaffdetailsForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from Registration.models import Staffdetails
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import *



def default(request):
    return render(request, 'Registration/Registration_01.html')


def index(request):
    return render(request,'Registration/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Homepage:home'))

@login_required
def special(request):
    return HttpResponse("You are logged in ,Nice!")

def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'Registration/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Homepage:home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'Registration/login.html',{})

def staff_registration(request):
    registered = False
    if request.method == "POST":
        staff_reg_form = StaffdetailsForm(request.POST)

        if staff_reg_form.is_valid():
            firstname = staff_reg_form.cleaned_data['firstname']
            lastname = staff_reg_form.cleaned_data['lastname']
            email = staff_reg_form.cleaned_data['email']
            password = staff_reg_form.cleaned_data['password']
            address = staff_reg_form.cleaned_data['address']
            pincode = staff_reg_form.cleaned_data['pincode']
            city = staff_reg_form.cleaned_data['city']
            employee_id = Staffdetails.emp_id()
            password = make_password(password)

            if not ((Staffdetails.objects.filter(firstname=firstname).exists() and Staffdetails.objects.filter(lastname=lastname).exists()) or Staffdetails.objects.filter(email=email).exists() or Staffdetails.objects.filter(employee_id=employee_id).exists()):
                Staffdetails.objects.create(firstname=firstname,lastname=lastname,email=email,password=password,address=address,pincode=pincode,city=city,employee_id=employee_id)
                registered = True

                staff_details = staff_reg_form.save(commit=False)

                return HttpResponse("Your employee id is {}" .format(employee_id))
            else :
                message = "An account with same firstname,lastname or email already exsts .Please try again"
                return render(request,'Registration/alert.html',{'message' :message})
                #return HttpResponse("An account with same firstname,lastname or email already exsts")
                #messages.info(request,'An account with same firstname,lastname or email already exsts')
                #raise forms.ValidationError("A firstname or lastname or email swith that inputs already exist")
        else:
            print(staff_reg_form.errors)
    else:
        staff_reg_form = StaffdetailsForm()
    return render(request, 'Registration/Registration_02.html',
                  {'staff_reg_form': staff_reg_form, 'registered': registered})

"""
=======
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from Registration.forms import UserForm,UserProfileInfoForm,StaffdetailsForm
from Registration.models import Staffdetails
# Create your views here.
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def default(request):
    return render(request, 'Registration/Registration_01.html')

def index(request):
    return render(request,'Registration/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Homepage:home'))

@login_required
def special(request):
    return HttpResponse("You are logged in ,Nice!")

def register(request):
    registered = False
    verified = False
    #email
    subject = "REGISTRATION SUCCESSFUL"

    message = "Hi .Thank You For Registering.Verify your email-id here by click this below link "
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            email = user.email
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            rergistered = True
            send_mail(subject,message, ['csa.ase1@gmail.com'],[email],html_message="<a href = http://127.0.0.1:8000/registration/email_verify>click here to verify your email</a>")

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'Registration/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Homepage:home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'Registration/login.html',{})


#staff registration

def staff_registration(request):
    registered = False
    message= "ok"
    if request.method == "POST":
        staff_reg_form = StaffdetailsForm(request.POST)

        if staff_reg_form.is_valid():
            firstname = staff_reg_form.cleaned_data['firstname']
            lastname = staff_reg_form.cleaned_data['lastname']
            email = staff_reg_form.cleaned_data['email']
            password = staff_reg_form.cleaned_data['password']
            address = staff_reg_form.cleaned_data['address']
            pincode = staff_reg_form.cleaned_data['pincode']
            employee_id = Staffdetails.emp_id()
            if not ((Staffdetails.objects.filter(firstname=firstname).exists() and Staffdetails.objects.filter(lastname=lastname).exists()) or Staffdetails.objects.filter(email=email).exists() or Staffdetails.objects.filter(employee_id=employee_id).exists()):
                Staffdetails.objects.create(firstname=firstname,lastname=lastname,email=email,password=password,address=address,pincode=pincode,employee_id=employee_id)
                registered = True
                staff_details = staff_reg_form.save(commit=False)
                return HttpResponse("Your employee id is {}" .format(employee_id))
            else :
                message = "An account with same firstname,lastname or email already exsts .Please try again"
                return render(request,'Registration/alert.html',{'message' :message})
                #return HttpResponse("An account with same firstname,lastname or email already exsts")
                #messages.info(request,'An account with same firstname,lastname or email already exsts')
                #raise forms.ValidationError("A firstname or lastname or email swith that inputs already exist")
        else:
            print(staff_reg_form.errors)
    else:
        staff_reg_form = StaffdetailsForm()
    return render(request, 'Registration/Registration_02.html',
                  {'staff_reg_form': staff_reg_form, 'registered': registered})  

count = 0
def cust_verify(self):
    global count
    count=count+1;
    return(count)

def email_verify(request):
    return render(request,'Registration/email_verify.html',{})

def email_verified(request):
    return HttpResponse("Your email is verified")

"""
#staff login
"""
def staff_login(request):
    staff = False
    if request.method=='POST':
        employee_id = Staffdetails.employee_id
        password = Staffdetails.password
        emplo_id=request.POST.get('employee_id')
        psw=request.POST.get('password')
        if (employee_id==emplo_id) and (password==psw):
            staff = True
        else:
            staff = False
    #here
    else :
        return render(request,'Registration/staff_login.html',{})

    
           if staff:
                if staff.is_active:
                    login(request,staff)
                    return HttpResponseRedirect(reverse('Homepage:home'))
                    return HttpResponse("You are logged in")
                else:
                    return HttpResponse("ACCOUNT NOT ACTIVE")
            else:
                return HttpResponse("invalid login details")
"""

