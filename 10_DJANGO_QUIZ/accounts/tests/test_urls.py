from accounts.views import AccountRegisterView
from accounts.views import account_profile_view

from django.test import SimpleTestCase
from django.urls import resolve
from django.urls import reverse


class TestUrls(SimpleTestCase):
    def test_registration_url_resolves(self):
        url = reverse('accounts:registration')
        self.assertEqual(resolve(url).func.view_class, AccountRegisterView)

    def test_profile_url_resolves(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func, account_profile_view)
