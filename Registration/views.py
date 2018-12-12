from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from Registration.forms import UserForm, UserProfileInfoForm, StaffdetailsForm, PasswordResetForm, SetNewPasswordForm, \
    AdmindetailsForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from Registration.models import Staffdetails, UserProfileInfo, Admin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import *

from Registration.tokens import account_activation_token


def default(request):
    return render(request, 'Registration/Registration_01.html')


def index(request):
    return render(request, 'Registration/index.html')


def user_logout(request):
    logout(request)
    return redirect('Homepage:home', category='all')


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
            send_mail(mail_subject, message, [
                'csa.ase1@gmail.com'], [to_email])
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
        user.is_active = True
    if user is not None and account_activation_token.check_token(user, token):
        user.save()
        username = user.username
        user_info = User.objects.get(username=username)
        user_info1 = UserProfileInfo.objects.get(user=user_info)
        user_info1.is_verified = True
        user_info1.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'Registration/Registered.html', {})
    else:
        print(user)
        print(account_activation_token.check_token(user, token))
        return HttpResponse('Activation link is invalid!')


def user_login(request):
    user_logged_in = False
    registered = True
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user1 = check_password(password, user.password)
            if user and user1:
                user_info = User.objects.get(username=username)
                user_info1 = UserProfileInfo.objects.get(user=user_info)
                if user_info1.is_verified is True:
                    request.session.set_expiry(900)
                    request.session['username'] = user.username
                    # login(request, user)
                    return redirect('Homepage:home', category='all')
                elif not user_info1.is_verified:
                    registered = False
                    user_logged_in = False
                    return render(request, 'Registration/login.html',
                                  {'user_logged_in': user_logged_in, 'registered': registered})
                else:
                    registered = False
                    return render(request, 'Registration/login.html',{'user_logged_in': user_logged_in, 'registered': registered})
            else:
                user_logged_in = False
                return render(request, 'Registration/login.html',{'user_logged_in': user_logged_in, 'registered': registered})
        except:
            registered = False
            return render(request, 'Registration/login.html',{'user_logged_in': user_logged_in, 'registered': registered})

    else:
        user_logged_in = True
        return render(request, 'Registration/login.html', {'user_logged_in':user_logged_in,'registered':registered})


def get_editprofile_dict(request, username):
    user = User.objects.filter(username=username)
    # print(user)
    userId = User.objects.get(username=username).id
    # user = User.objects.filter(username=request.user)
    userprofileinfo = UserProfileInfo.objects.filter(id=userId)
    context = {
    }
    # print(user.values())
    for field in user.values():
        context["user"] = field
    for field in userprofileinfo.values():
        context["userprofileinfo"] = field
    return context


def change_user_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('Email')
            user = User.objects.get(email=email)
            if user:
                # socket.getaddrinfo('localhost', 8080)
                current_site = get_current_site(request)
                mail_subject = 'Reset Your Password'
                message = render_to_string('Registration/password_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('Email')
                send_mail(mail_subject, message, ['csa.ase1@gmail.com'], [to_email])
                return render(request, 'Registration/password_reset_done.html', {})
            else:
                return HttpResponse('Email does not exist')
        else:
            return HttpResponse('Please enter a valid email')
    else:
        form = PasswordResetForm()
        return render(request, 'Registration/password_reset_form.html', {'form': form, 'user': "1"})


def user_password_reset(request, uidb64, token):
    if request.method == 'POST':
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('Password')
            password2 = form.cleaned_data.get('Confirm_Password')
            if password1 == password2:
                try:
                    uid = urlsafe_base64_decode(uidb64).decode()
                    user = User.objects.get(pk=uid)
                except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                    user = None
                if user is not None and account_activation_token.check_token(user, token):
                    user.set_password(password1)
                    user.save()
                    return HttpResponse('Your Password is changed successfully')
                else:
                    return HttpResponse('Invalid reset link')
            else:
                return HttpResponse('Password does not match')
        else:
            return render(request, 'Registration/password_reset_confirm.html', {'form': form})
    else:
        form = SetNewPasswordForm()
        return render(request, 'Registration/password_reset_confirm.html', {'form': form})


def editprofile(request, username):
    context = get_editprofile_dict(request, username)
    return render(request, 'Registration/editprofile.html', context=context)
    # return HttpResponse("user")


def change_profile_info(request, username):
    new_password = request.POST['new_password']
    new_password_conf = request.POST['new_password_conf']
    print(new_password)
    print(new_password_conf)
    userprofileinfo = UserProfileInfo.objects.get(user__username=username)
    old_password_check = userprofileinfo.user.check_password(
        request.POST['old_password'])
    print(userprofileinfo.user.check_password(request.POST['old_password']))
    if not (new_password == new_password_conf or old_password_check == True):
        return False
    print(userprofileinfo.user.check_password(request.POST['old_password']))
    if new_password != '':
        if not(new_password == new_password_conf or old_password_check == True):
            return False
    print("some")
    userprofileinfo.user.email = request.POST['email']
    userprofileinfo.user.first_name = request.POST['first_name']
    userprofileinfo.user.last_name = request.POST['last_name']
    userprofileinfo.address = request.POST['address']
    userprofileinfo.city = request.POST['city']
    userprofileinfo.pincode = request.POST['pincode']
    if 'profile_pic' in request.FILES:
        print("profile pic exists")
        userprofileinfo.profile_pic = request.FILES['profile_pic']
    if new_password != '':
        userprofileinfo.user.set_password(request.POST['new_password'])
    userprofileinfo.user.save()
    userprofileinfo.save()
    #userprofileinfo = UserProfileInfo.objects.get(user__username = username)
    #print(userprofileinfo.user.username)
    return True


#@login_required
def updateprofile(request, username):
    valid_profile_data = change_profile_info(request, username)
    # print(valid_profile_data)
    if valid_profile_data == False:
        context = get_editprofile_dict(request, username)
        context['match_failed'] = True
        context['message'] = "Your old password didn't match or your new passwords didn't match with each other"
        return render(request, 'Registration/editprofile.html', context=context)
    values = UserProfileInfo.objects.filter(
        user__username=username)
    print(values)
    context = {
        'user_id': values[0]
    }
    return render(request, 'Registration/updatedprofile.html', context=context)


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
            password_old = password
            password = make_password(password)

            if not ((Staffdetails.objects.filter(firstname=firstname).exists() and Staffdetails.objects.filter(
                    lastname=lastname).exists()) or Staffdetails.objects.filter(
                email=email).exists() or Staffdetails.objects.filter(employee_id=employee_id).exists()):
                Staffdetails.objects.create(firstname=firstname, lastname=lastname, email=email, password=password,
                                            address=address, pincode=pincode, city=city, employee_id=employee_id)
                registered = True
                staff_details = staff_reg_form.save(commit=False)
                mail_subject = "Registration successful"
                message = "You are successfully registered with us as staff.login with username :{}, password:{} ".format(
                    employee_id, password_old)
                send_mail(mail_subject, message, ['csa.ase1@gmail.com'], [email])
                return redirect('Manager:staff_home')
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
    registered = True
    if request.method == 'POST':
            employee_id = request.POST.get('employee_id')
            password = request.POST.get('password')
            try:
                staff = Staffdetails.objects.get(employee_id=employee_id)
                staff_log = check_password(password, staff.password)
                if staff_log:
                    # login(request,staff)
                    request.session['employee_id'] = staff.employee_id
                    staff_logged_in = True
                    # request.session['staff_fname'] = staff.firstname
                    return HttpResponseRedirect(reverse('Manager:index'))
                # return HttpResponse("you are logged in {}".format(staff.firstname))
                # return render(request, 'Registration/staff_login.html', {})

                else:
                    staff_logged_in = False
                    return render(request, 'Registration/staff_login.html', {'staff_logged_in': staff_logged_in,'registered': registered})
            except:
                registered = False
                return render(request, 'Registration/staff_login.html', {'staff_logged_in': staff_logged_in,'registered':registered})
    else:
        staff_logged_in = True
        return render(request, 'Registration/staff_login.html', {'staff_logged_in': staff_logged_in,'registered':registered})




def staff_logout(request):
    try:
        del request.session['employee_id']
    except KeyError:
        return HttpResponse("You are not logged in")
    return redirect('Homepage:home', category='all')

def test(request):
    editadmin(request, 'ADMN001')


def editadmin(request, admin_id):
    admin = Admin.objects.filter(admin_id=admin_id)
    context = {'admin': admin}
    return render(request, 'Registration/editadmin.html', context)


def change_admin_info(request, admin_id):
    admin = Admin.objects.get(admin_id=admin_id)
    print(check_password(request.POST['old_password'], admin.password))
    if (check_password(request.POST['old_password'], admin.password) == False):
        return False
    if request.POST['new_password'] != request.POST['new_password_conf']:
        return False

# @login_required
def editadmin(request):
    admin = Admin.objects.filter(Name="test_admin")
    context = admin.values()
    context = context[0]
    return render(request, 'Registration/editadmin.html', context=context)


# @login_required
def updateadmin(request):
    admin = Admin.objects.get(Name="test_admin")
    admin.Name = request.POST['Name']
    admin.email = request.POST['email']
    # updating password if the new password is not empty
    if request.POST['new_password'] != '':
        admin.password = make_password(request.POST['new_password'])
    admin.canteen_name = request.POST['canteen_name']
    admin.canteen_street = request.POST['canteen_street']
    admin.canteen_pincode = request.POST['canteen_pincode']
    admin.save()
    return True


def updateadmin(request, admin_id):
    changed_status = change_admin_info(request, admin_id)
    if changed_status:
        context = Admin.objects.filter(admin_id=admin_id)
        print(context)
        return HttpResponse('Saved')
        return render(request, 'Registration/updatedadmin.html', context=context)
    return HttpResponse('Failed')


#@login_required
def editstaff(request, employee_id):
    staff = Staffdetails.objects.filter(employee_id=employee_id)
    context = staff.values()
    context = context[0]
    print(context)
    return render(request, 'Registration/editstaff.html', context=context)
    #return HttpResponse('Saved')



def updatestaff(request, employee_id):
    staff = Staffdetails.objects.get(employee_id=employee_id)
    staff['lastname'] = request.POST['lastname']
    staff['email'] = request.POST['email']
    staff['pincode'] = request.POST['pincode']
    staff['firstname'] = request.POST['firstname']
    staff['address'] = request.POST['address']
    staff['city'] = request.POST['city']
    staff.save()
    return HttpResponse("Updated Staff Page")


def admin_register(request):
    registered = False
    if request.method == "POST":
        is_present = Admin.objects.all()
        admin_reg_form = AdmindetailsForm(request.POST)
        if not is_present:
            if admin_reg_form.is_valid():
                Name = admin_reg_form.cleaned_data['Name']
                username = admin_reg_form.cleaned_data['username']
                email = admin_reg_form.cleaned_data['email']
                password = admin_reg_form.cleaned_data['password1']
                canteen_name = admin_reg_form.cleaned_data['canteen_name']
                canteen_street = admin_reg_form.cleaned_data['canteen_street']
                canteen_pincode = admin_reg_form.cleaned_data['canteen_pincode']
                canteen_city = admin_reg_form.cleaned_data['canteen_city']
                password = make_password(password)

                Admin.objects.create(Name=Name, email=email, username=username, password=password,
                                     canteen_street=canteen_street,
                                     canteen_name=canteen_name, canteen_pincode=canteen_pincode,
                                     canteen_city=canteen_city)

                registered = True

                Admin_details = admin_reg_form.save(commit=False)

                return redirect('Registration:admin_login')
            else:
                print(admin_reg_form.errors)

        else:
            registered = True
            return render(request, 'Registration/Admin_Registration.html',
                          {'admin_reg_form': admin_reg_form, 'registered': registered})
    else:
        admin_reg_form = AdmindetailsForm()
    return render(request, 'Registration/Admin_Registration.html',
                  {'admin_reg_form': admin_reg_form, 'registered': registered})


def admin_login(request):
    admin_logged_in = False
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            admin = Admin.objects.get(username=username)
            admin_log = check_password(password, admin.password)
        except:
            return redirect('Registration:admin_reg')
        if admin_log:
            # login(request,staff)
            request.session['admin_id'] = admin.admin_id
            admin_logged_in = True
            return HttpResponseRedirect(reverse('Manager:index'))
        else:
            return render(request, 'Registration/admin_not_log.html', {})
    else:
        return render(request, 'Registration/admin_login.html', {})


def admin_logout(request):
    try:
        del request.session['admin_id']
    except KeyError:
        return redirect('Homepage:home', category="all")
    return redirect('Homepage:home', category="all")


