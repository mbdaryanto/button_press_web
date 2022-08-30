from django.test import TestCase, Client

class CounterTestCast(TestCase):
    def test_user_register_login(self):
        c = Client()
        response = c.get('/counter', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json()['counter'], 0)

        response = c.post('/members/register_user', { 'username': 'randomusername', 'password1': 'supersimplepassword', 'password2': 'supersimplepassword'}, follow=True)
        self.assertEqual(response.status_code, 200)

        response = c.get('/counter', follow=True)
        self.assertEqual(response.status_code, 200)
        counter = response.json()['counter']

        for _ in range(5):
            response = c.post('/increment', follow=True)
            self.assertEqual(response.status_code, 200)
            next_counter = response.json()['counter']

            self.assertEqual(counter + 1, next_counter)
            counter = next_counter

        # after increment 5 times consecutively (less than 60 secs = assumption)
        response = c.post('/increment', follow=True)
        self.assertNotEqual(response.status_code, 200)




