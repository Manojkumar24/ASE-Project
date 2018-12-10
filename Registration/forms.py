from django import forms
from Registration.models import UserProfileInfo, Staffdetails
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    # password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    email = forms.EmailField(max_length=200, required=True)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    """def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        else:
            return password2
"""


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('address', 'city', 'pincode', 'profile_pic')


class StaffdetailsForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    email = forms.EmailField(max_length=200, required=True)

    class Meta():
        model = Staffdetails
        fields = ('firstname', 'lastname', 'email', 'password1', 'password2', 'address', 'city', 'pincode')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class PasswordResetForm(forms.Form):
    Email = forms.EmailField(label='Email',help_text="Please enter the email with which you have registered.")
    fields = 'Email'


class SetNewPasswordForm(forms.Form):
    Password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())
