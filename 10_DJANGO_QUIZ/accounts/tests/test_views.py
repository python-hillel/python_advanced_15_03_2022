from unittest import skip

from django.contrib.auth.models import Group

from accounts.models import CustomUser

from django.core.signing import Signer
from django.test import Client
from django.test import TestCase
from django.urls import reverse


class AccountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Users')

    def setUp(self) -> None:
        self.data = {
            'username': 'user_1',
            'password1': '123qwe!@#',
            'password2': '123qwe!@#',
            'email': 'user_1@test.com'
        }
        self.client = Client()
        self.registration_url = reverse('accounts:registration')
        self.registration_done_url = reverse('accounts:register_done')

    # @skip
    def test_registration_valid(self):
        response = self.client.post(self.registration_url, self.data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.registration_done_url, status_code=302, target_status_code=200)
        self.assertEqual(response.url, self.registration_done_url)

        user = CustomUser.objects.first()
        self.assertEqual(user.username, self.data['username'])
        self.assertEqual(user.email, self.data['email'])
        self.assertTrue(user.check_password(self.data['password1']))
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_activated)

    # @skip
    def test_registration_invalid(self):
        self.data['password2'] = '123qwe!@'

        response = self.client.post(self.registration_url, self.data)
        self.assertNotEqual(response.status_code, 302)
        self.assertFalse(response.context['form'].is_valid())
        user = CustomUser.objects.filter(username=self.data['username'])
        self.assertEqual(len(user), 0)

    # @skip
    def test_activation_url(self):
        response = self.client.post(self.registration_url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.registration_done_url, status_code=302, target_status_code=200)

        user = CustomUser.objects.first()
        self.assertEqual(user.username, self.data['username'])

        signer = Signer()
        response = self.client.get('http://localhost' + reverse('accounts:register_activate', kwargs={'sign': signer.sign(user.username)}))
        self.assertEqual(response.status_code, 200)

        user.refresh_from_db()
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_activated)
