from django.test import TestCase, Client
from django.urls import reverse


class MemberTestCast(TestCase):
    def test_user_register_login(self):
        c = Client()
        response = c.post('/members/register_user', { 'username': 'randomusername', 'password1': 'supersimplepassword', 'password2': 'supersimplepassword'}, follow=True)
        self.assertEqual(response.status_code, 200)

        response = c.get('/members/logout_user', follow=True)
        self.assertEqual(response.status_code, 200)

        response = c.post('/members/login_user', { 'username': 'randomusername', 'password': 'supersimplepassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
