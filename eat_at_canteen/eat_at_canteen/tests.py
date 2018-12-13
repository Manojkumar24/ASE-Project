from django.http import request
from django.test import TestCase,Client
from django.contrib.auth.models import User
from .models import Review
import datetime


class Test_Models(TestCase):

        def Create_model1(self):
            user = User.objects.create(username='john')
            return Review.objects.create(user_id=user,pub_date=datetime.datetime.now(),user_name=user.username,comment='Good',rating=5)

        def test_models(self):
            a=self.Create_model1()
            self.assertTrue(isinstance(a,Review))
'''class Test_Models1(TestCase):
    def Create_model2(self, Date = "2018-09-23",price = "5"):
         return new2.objects.create(Date=Date,
         price=price)



    def test_models2(self):
         a=self.Create_model2()
         self.assertTrue(isinstance(a,new2))
'''

