from django.test import TestCase,Client
from django.contrib.auth.models import User
from history.models import *

class Test_Models(TestCase):


    def Create_model1(self, item = "item1",frequency = "5"):
        return new1.objects.create(item=item,
        frequency=frequency)



    def test_models(self):
        a=self.Create_model1()
        self.assertTrue(isinstance(a,new1))
class Test_Models1(TestCase):
    def Create_model2(self, Date = "2018-09-23",price = "5"):
         return new2.objects.create(Date=Date,
         price=price)



    def test_models2(self):
         a=self.Create_model2()
         self.assertTrue(isinstance(a,new2))
