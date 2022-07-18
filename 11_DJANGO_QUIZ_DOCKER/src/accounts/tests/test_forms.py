from accounts.forms import AccountRegisterForm

from django.test import TestCase


class TestForms(TestCase):
    def setUp(self):
        self.username = 'user_1'
        self.password = '123qwe!@#'
        self.email = 'user_1@test.com'

    def test_registration_form_valid_data(self):
        form = AccountRegisterForm(
            data={
                'username': self.username,
                'email': self.email,
                'password1': self.password,
                'password2': self.password
            }
        )

        self.assertTrue(form.is_valid())

    # @skip
    def test_registration_form_no_data(self):
        form = AccountRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_registration_form_without_passwords_raise_exception(self):
        form = AccountRegisterForm(data={
                'username': self.username,
                'email': self.email,
                'password1': self.password,
                'password2': 'self.password1'
            })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
