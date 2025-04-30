from django.test import TestCase
from accounts.models import User

class TestCreateUser(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email="user@test.com" ,
            password="hassan98"
        )
        self.assertEqual(user.email ,"user@test.com")