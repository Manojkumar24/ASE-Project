import string
from random import *
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #portfolio_site=models.URLField(blank=True)
    address = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=100,default='')
    pincode = models.CharField(max_length=6,default='')
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    """def __str__(self):
        return self.user.username
"""
class Admin(models.Model):
    Name = models.CharField(max_length=225,blank=False)
    email = models.EmailField()
    password = models.CharField(max_length = 50,null=True)
    canteen_name = models.CharField(max_length = 200,null=True)
    canteen_street = models.CharField(max_length=200,null=True)
    canteen_pincode = models.IntegerField(null=True)

"""class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
   # profile_pic = models.ImageField(upload_to='user_profile_pics',blank=True)
   """

class Staffdetails(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    employee_id = models.CharField(primary_key=True,max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    #password2 = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    pincode = models.CharField(max_length=6,default='')

    @classmethod
    def emp_id(self):
        min_char = 5
        max_char = 5
        #allchar = string.ascii_letters + string.punctuation + string.digits
        allchar = string.digits
        emp_id = "CSA"+ ("".join(choice(allchar) for x in range(randint(min_char, max_char))))
        return (emp_id)
    # Here be code
