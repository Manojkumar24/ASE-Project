from django.http import request
from django.test import TestCase,Client
from django.contrib.auth.models import User
from eat_at_canteen.models import *
import datetime


class Test_Models(TestCase):

        def Create_model1(self):
            user = User.objects.create(username='john')

            return Review.objects.create(user_id=user,pub_date=datetime.datetime.now(),user_name=user.username,comment='Good',rating=5)
        def test_models(self):
            a=self.Create_model1()
class Test_Models1(TestCase):

        def Create_model2(self):
            user = User.objects.create(username='john')
            return user_review.objects.create(user_id=user,user_name=user.username,latest_review='GOOD',latest_pub_date='2018-09-3',No_Reviews='2',average_rating=5)

        def test_models1(self):
            a=self.Create_model2()
