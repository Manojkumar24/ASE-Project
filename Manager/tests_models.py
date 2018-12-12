from django.test import TestCase,Client
from django.contrib.auth.models import User
from Manager.models import *
from django.core.files.uploadedfile import SimpleUploadedFile

class Test_manager_Models(TestCase):


    def Create_model1(self, Table_id='2',availability='True',size='2',zone='Normal'):
        return Dining_Tables.objects.create(Table_id=Table_id,availability=availability,size=size,zone=zone)



    def test_models(self):
        a=self.Create_model1()
        self.assertTrue(isinstance(a,Dining_Tables))
class Test_manager1_Models(TestCase):


    def Create_model1(self, Towns='sricity',pincode='517646'):
        return Available_Towns.objects.create(Towns=Towns,pincode=pincode)



    def test_models(self):
        a=self.Create_model1()
        self.assertTrue(isinstance(a,Available_Towns))
