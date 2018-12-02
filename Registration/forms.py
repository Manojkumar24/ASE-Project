from django import forms
from Registration.models import UserProfileInfo,Staffdetails
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=200,required=True)
    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('address','city','pincode','profile_pic')

class StaffdetailsForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=200,required=True)
    class Meta():
        model = Staffdetails
        fields = ('firstname','lastname','email','password','address','city','pincode')


"""class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('firstname','lastname','email','password','address','city')
=======
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Registration.models import UserProfileInfo,Staffdetails
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=200,required=True)
    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('address','city','pincode','profile_pic')

class StaffdetailsForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=200,required=True)
    class Meta():
        model = Staffdetails
        fields = ('firstname','lastname','email','password','address','pincode')
"""


"""
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('firstname','lastname','email','password','address','city')
"""