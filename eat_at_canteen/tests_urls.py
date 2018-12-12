from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.





class Testeat_at_canteen_Url(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/cart/'



    def test_anonymous_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)
        # self.assetRedirects(response,expected_url='/registration/user_login/?next=/ec/cart/')


    def test_authenticated_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/cart/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/cart/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url1(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/index/'


    def test_anonymous_ping(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        # self.assertEqual(response.status_code,200)
        self.assertEqual(response.status_code,200)

    def test_anonymous_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)
        # self.assetRedirects(response,expected_url='/registration/user_login/?next=/ec/cart/')


    def test_authenticated_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/index/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/index/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url2(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/checkout/'



    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/checkout/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/checkout/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url3(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/table/'



    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/table/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/table/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url4(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/orderfood/'



    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/orderfood/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/orderfood/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url5(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/update/'



    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/update/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/update/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url6(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/delete/'



    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/delete/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/delete/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url7(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/confirm/'



    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/confirm/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/confirm/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url8(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None

        self.request_url = '/ec/remove/'


    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/remove/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/remove/blahblah')
        self.assertEqual(response.status_code, 404)
class Testeat_at_canteen_Url9(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/ec/add/'



    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/ec/add/blahblah')
        self.assertEqual(response.status_code, 404)



    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/ec/add/blahblah')
        self.assertEqual(response.status_code, 404)
