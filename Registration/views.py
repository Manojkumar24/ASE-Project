from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from Registration.forms import UserForm, UserProfileInfoForm, StaffdetailsForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from Registration.models import Staffdetails, UserProfileInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import *

from Registration.tokens import account_activation_token


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
            user.is_active = False
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            current_site = get_current_site(request)
            mail_subject = 'Thanks for registering.Activate your account here.'
            message = render_to_string('Registration/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.email
            print(user.email)
            send_mail(mail_subject, message,['csa.ase1@gmail.com'],[to_email])
            return HttpResponse('Please confirm your email address to complete the registration')


        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'Registration/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        username = user.username
        user_info = User.objects.get(username=username)
        user_info1 = UserProfileInfo.objects.get(user = user_info)
        user_info1.is_verified = True
        user_info1.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user :
            user_info = User.objects.get(username=username)
            user_info1 = UserProfileInfo.objects.get(user=user_info)
            if user.is_active and (user_info1.is_verified==True):
                request.session.set_expiry(900)
                login(request, user)
                return HttpResponseRedirect(reverse('Homepage:home'))
            elif user_info1.is_verified==False:
                return HttpResponse("If you have already registered with us but not yet confirmed your email id,Please verify your email id to proceed .")
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        elif not user:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'Registration/login.html', {})


def staff_registration(request):
    registered = False
    if request.method == "POST":
        staff_reg_form = StaffdetailsForm(request.POST)

        if staff_reg_form.is_valid():
            firstname = staff_reg_form.cleaned_data['firstname']
            lastname = staff_reg_form.cleaned_data['lastname']
            email = staff_reg_form.cleaned_data['email']
            password = staff_reg_form.cleaned_data['password1']
            address = staff_reg_form.cleaned_data['address']
            pincode = staff_reg_form.cleaned_data['pincode']
            city = staff_reg_form.cleaned_data['city']
            employee_id = Staffdetails.emp_id()
            password = make_password(password)

            if not ((Staffdetails.objects.filter(firstname=firstname).exists() and Staffdetails.objects.filter(
                    lastname=lastname).exists()) or Staffdetails.objects.filter(
                email=email).exists() or Staffdetails.objects.filter(employee_id=employee_id).exists()):
                Staffdetails.objects.create(firstname=firstname, lastname=lastname, email=email, password=password,
                                            address=address, pincode=pincode, city=city, employee_id=employee_id)
                registered = True

                staff_details = staff_reg_form.save(commit=False)

                return HttpResponse("Your employee id is {}".format(employee_id))
            else:
                message = "An account with same firstname,lastname or email already exsts .Please try again"
                return render(request, 'Registration/alert.html', {'message': message})
                # return HttpResponse("An account with same firstname,lastname or email already exsts")
                # messages.info(request,'An account with same firstname,lastname or email already exsts')
                # raise forms.ValidationError("A firstname or lastname or email swith that inputs already exist")
        else:
            print(staff_reg_form.errors)
    else:
        staff_reg_form = StaffdetailsForm()
    return render(request, 'Registration/Registration_02.html',
                  {'staff_reg_form': staff_reg_form, 'registered': registered})


def staff_login(request):
    staff_logged_in = False
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')
        staff = Staffdetails.objects.get(employee_id=employee_id)
        staff_log = check_password(password, staff.password)
        if staff_log:
            # login(request,staff)
            request.session['employee_id'] = staff.employee_id
            staff_logged_in = True
            # request.session['staff_fname'] = staff.firstname
            return HttpResponseRedirect(reverse('Homepage:home'))
            # return HttpResponse("you are logged in {}".format(staff.firstname))
            # return render(request, 'Registration/staff_login.html', {})
        else:
            return HttpResponse("Not logged in")
    else:
        return render(request, 'Registration/staff_login.html', {})


"""def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")
"""


def staff_logout(request):
    try:
        del request.session['employee_id']
    except KeyError:
        return HttpResponse("You are not logged in")
    return HttpResponseRedirect(reverse('Homepage:home'))
