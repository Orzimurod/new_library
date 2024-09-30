from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def test_login_view_status_code(self):
        # Make a GET request to the login view
        response = self.client.get(reverse('login'))  # Ensure 'login' is the correct URL name
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
