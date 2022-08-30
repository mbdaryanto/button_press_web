from django.test import TestCase, Client
from django.urls import reverse


class MemberTestCast(TestCase):
    def test_user_register_login(self):
        c = Client()
        # As a user I can register an account on the Button Press website
        response = c.post('/members/register_user', { 'username': 'randomusername', 'password1': 'supersimplepassword', 'password2': 'supersimplepassword'}, follow=True)
        self.assertEqual(response.status_code, 200)

        # As a user I can log out of the Button Press website
        response = c.get('/members/logout_user', follow=True)
        self.assertEqual(response.status_code, 200)

        # As a user I can login to the Button Press website
        response = c.post('/members/login_user', { 'username': 'randomusername', 'password': 'supersimplepassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
