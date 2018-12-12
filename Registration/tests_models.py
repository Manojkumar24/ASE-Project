from django.test import TestCase,Client
from django.contrib.auth.models import User
from Registration.models import *

class Test_Registration_Models(TestCase):


    def Create_model1(self, Name='neeharika',email='neeharika149@gmail.com',password='gfdd',canteen_name='canteen',canteen_street='sricity',canteen_pincode='517646'):
        return Admin.objects.create(Name=Name,email=email,password=password,canteen_name=canteen_name,canteen_street=canteen_street,canteen_pincode=canteen_pincode)




    def test_models(self):
        a=self.Create_model1()
        self.assertTrue(isinstance(a,Admin))
class Test_Registration_Models1(TestCase):
    def Create_model2(self, firstname='devi',lastname='neeharika',employee_id='2',email='neeharika149@gmail.com',password='gfdd',address='dsdsss',city='sricty'):
         return Staff.objects.create(firstname=firstname,lastname=lastname,employee_id=employee_id,email=email,password=password,address=address,city=city)




    def test_models2(self):
         a=self.Create_model2()
         self.assertTrue(isinstance(a,Staff))
