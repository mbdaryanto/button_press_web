import time
from django.test import TestCase, Client


class CounterTestCast(TestCase):
    def test_counter_increment(self):
        c = Client()
        # As a non-logged in user, I can see the total number of clicks
        response = c.get('/counter', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json()['counter'], 0)

        # As a non-logged in user, I cannot access increment
        response = c.post('/increment', follow=True)
        self.assertNotEqual(response.status_code, 200)

        # As a user I can register an account on the Button Press website
        response = c.post('/members/register_user', { 'username': 'randomusername', 'password1': 'supersimplepassword', 'password2': 'supersimplepassword'}, follow=True)
        self.assertEqual(response.status_code, 200)

        response = c.get('/counter', follow=True)
        self.assertEqual(response.status_code, 200)
        counter = response.json()['counter']

        # successfully increment 5 times consecutively
        for _ in range(5):
            response = c.post('/increment', follow=True)
            self.assertEqual(response.status_code, 200)
            next_counter = response.json()['counter']

            self.assertEqual(counter + 1, next_counter)
            counter = next_counter

        # after increment 5 times consecutively (less than 60 secs = assumption)
        response = c.post('/increment', follow=True)
        self.assertNotEqual(response.status_code, 200)

        time.sleep(60)

        # after 60 seconds user allowed to increment
        response = c.post('/increment', follow=True)
        self.assertEqual(response.status_code, 200)




