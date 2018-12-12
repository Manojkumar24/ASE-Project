from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.
class TestHomedeliveryUrl(TestCase):

    def setUp(self):

        self.createadmin = User.objects.create_user(username = "test user", email = "test@gmail.com", password = "test password")

        self.client = None
        self.request_url = '/homedelivery/address/'


    def test_anonymous_ping(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        # self.assertEqual(response.status_code,200)
        self.assertRedirects(response, expected_url='/registration/user_login/?next=/homedelivery/address/')
    def test_authenticated_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_random_id_ping(self):
        self.client = Client()
        response = self.client.get('/homedelivery/address/blahblah')
        self.assertEqual(response.status_code, 404)




    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createadmin)
        response = self.client.get('/homedelivery/address/blahblah')
        self.assertEqual(response.status_code, 404)
