from django.contrib.auth.models import User
from django.test import TestCase, Client


class LoginTest(TestCase):
    client = Client()

    def true_test(self):
        self.assertTrue(True)

    def test_login_success(self):
        User.objects.create_user('imie', 'raz@dwa.pl', 1).save()
        response = self.client.post('/login/auth/', {'inputEmail': 'raz@dwa.pl', 'inputPassword': 1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_login_fail(self):
        User.objects.create_user('imie', 'raz@dwa.pl', 1).save()
        response = self.client.post('/login/auth/', {'inputEmail': 'blabla@wp.pl', 'inputPassword': 123})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

if __name__ == '__main__':
    TestCase.main()