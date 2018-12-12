from django.http import request
from django.test import TestCase,Client
from django.contrib.auth.models import User
from homedelivery.models import *
from User.models import *
import datetime


# class Test_Models1(TestCase):
#
#         def Create_model1(self):
#             tokenid = Order_User.objects.create(TokenId='20170012')
#
#             return HD_Address.objects.create(tokenId=tokenid.TokenId,town='sricity',street='ght',dNo='6-7',phone_number='9491134791')
#         def test_models(self):
#             a=self.Create_model1()
