from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def test_login_view_status_code(self):
        response = self.client.get