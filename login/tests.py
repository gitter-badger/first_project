from django.contrib.auth.models import User
from django.test import TestCase, Client


class LoginTest(TestCase):
    client = Client()

    def true_test(self):
        self.assertTrue(True)

    def test_login_success(self):
        User.objects.create_user('imie', 'raz@dwa.pl', 1)
        response = self.client.post('/login/auth/', {'inputEmail': 'raz@dwa.pl', 'inputPassword': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logged_in_simple_text.html')

    def test_login_fail(self):
        User.objects.create_user('imie', 'raz@dwa.pl', 1)
        response = self.client.post('/login/auth/', {'inputEmail': 'blabla@wp.pl', 'inputPassword': 123})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/failed.html')

if __name__ == '__main__':
    TestCase.main()