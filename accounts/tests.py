from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignUpPageTests(TestCase):

    def test_sign_up_view_name(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_sign_up_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'tester',
                'email': 'testuser@email.com',
                'password1': 'testpass123',
                'password2': 'testpass123',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email,"testuser@email.com")
        self.assertEqual(get_user_model().objects.all()[0].username,"tester") #not working, need to research why