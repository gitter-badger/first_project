from django.test import TestCase, Client

# Create your tests here.
class FormResponseTest(TestCase):
    client = Client()

    def true_test(self):
        self.assertTrue(True)

    def test_return_success(self):
        response = self.client.post('/form_response/', {'event_name': 'test_event_1', 'registration_status': "true"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration_successful.html')

    def test_return_fail(self):
        response = self.client.post('/form_response/', {'event_name': 'test_event_2', 'registration_status': "false", 'registration_failure_reason': 'because fuck you'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration_failed.html')

if __name__ == '__main__':
    TestCase.main()