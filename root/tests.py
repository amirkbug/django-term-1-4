from django.test import TestCase , Client
from django.urls import resolve , reverse
from root.views import HomeView , contactus , AboutView
from root.forms import ContactUsForm
from accounts.models import User


class Testroot(TestCase):
    def test_url_home(self):
        url = reverse("root:home")
        self.assertEqual(resolve(url).func.view_class, HomeView)


    def test_url_contact(self):
        url = reverse("root:contact")
        self.assertEqual(resolve(url).func, contactus)


    def test_url_about(self):
        url = reverse("root:about")
        self.assertEqual(resolve(url).func.view_class , AboutView)



class TestResponse(TestCase):

    # def test_response_home(self):
    #     url = reverse("root:home")
    #     client = Client()
    #     response = client.get(url)
    #     self.assertEqual(response.status_code , 200)


        
    def test_response_home(self):
        url = reverse("root:home")
        user = User.objects.create_user(email="hassan@gmail.com" , password="hassan539")
        client = Client()
        client.force_login(user)
        response = client.get(url)
        self.assertEqual(response.status_code , 200)






class TestTemplate(TestCase):
    def test_template_home(self):
        url = reverse("root:home")
        user = User.objects.create_user(email="hassan@gmail.com" , password="hassan539")
        client = Client()
        client.force_login(user)
        response = client.get(url)
        self.assertTemplateUsed(response , template_name="root/index.html")
        


class TestForm(TestCase):
    def test_form_contact(self):
        form = ContactUsForm(data={
            "name" : "hassan",
            "email" : "email@gmail.com",
            "subject" : "test",
            "message" : "salam",
        })
        self.assertTrue(form.is_valid())



    def test_form_contact_invalid(self):
        form = ContactUsForm(data={
            "name" : None,
            "email" : "email@gmail.com",
            "subject" : "test",
            "message" : "salam",
        })
        self.assertFalse(form.is_valid())
        
