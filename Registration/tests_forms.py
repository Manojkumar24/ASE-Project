from django.test import Client,TestCase
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image

class DocumentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@gmail.com", password="Hello World")
        def create_Model(self, address="address", city="sricity",pincode="517646", profile_pic="beach1.jpg"):
         user = UserProfileInfo(user=User)
         return UserProfileInfo.objects.create(address=address,city=city,pincode=pincode,profile_pic=profile_pic)

    def test_model_creation(self):
        self.assertTrue((self.user, 'image_set'))
class ModelFormTest1(TestCase):
    def test_valid_form_data(self):
        image_io = BytesIO() # BytesIO has to be used, StrinIO isn't working
        image = Image.new(mode='RGB', size=(200, 200))
        image.save(image_io, 'JPEG')
        form_data = {
                'address': "sricity",'city':"sricity",'pincode':"536243"
            }
        image_data = {
            'image_field': InMemoryUploadedFile(image_io, None, 'randomimage.jpg', 'apple/jpeg', len(image_io.getvalue()), None)
        }
        form = UserProfileInfoForm(data=form_data, files=image_data)
        self.assertTrue(form.is_valid())
class ModelFormTest2(TestCase):
    def test_valid_form_data(self):
        form_data={
        'username':"username",'first_name':"devi",'last_name':"neeharika",'email':"neeharika149@gmail.com",'password':"neeharika"
        }
        form=UserForm(data=form_data)
        self.assertTrue(form.is_valid())
