from django.test import TestCase,Client
from django.contrib.auth.models import User
from User.models import *
from Manager.models import*

class Test_User_Models(TestCase):


    def Create_model1(self, mailId="neeharika149@gmail.com",TokenId='2',status='ordered',totalPrice='24'):
        return Order_User.objects.create(mailId=mailId,TokenId=TokenId,status=status,totalPrice=totalPrice)



    def test_models(self):
        a=self.Create_model1()
        self.assertTrue(isinstance(a,Order_User))
# class Test_User_Models1(TestCase):
#
#
#      def Create_model1(self):
#          foodid = Food_items.objects.create(Food_id='2')
#
#          return Order_Food.objects.create(TokenId='2',FoodId=foodid.Food_id,quantity='2',price='30',TableId='3',Status='draft',date='2018-09-2',time='12:00')
#      def test_models1(self):
#          a=self.Create_model1()
