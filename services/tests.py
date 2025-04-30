from django.test import TestCase , Client
from services.forms import CommentForm
from services.models import Services
from accounts.models import User

# Create your tests here.


# class TestForm(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(email="user@test.com" , password="amir1384")


    # def test_form_comment(self):
    #     user = self.user
    #     services = Services.objects.create(
    #         title="hassani",
    #         agent = "<create an obnject of agent>",
    #     )
    #     form = CommentForm({
    #         "name" : "user", #va baghi chis haii ke mikhad

    #     })
    #     self.assertTrue()