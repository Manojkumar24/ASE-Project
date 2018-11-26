from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=100,default='')
    pincode = models.CharField(max_length=6,default='')

    profile_pic=models.ImageField(upload_to='static/registration/profile_pics',blank=True)

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

class Staff(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    employee_id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
