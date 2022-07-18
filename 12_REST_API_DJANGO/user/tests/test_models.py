from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTest(TestCase):
    def test_create_user_with_email_success(self):
        email = 'user_1@test.com'
        password = '123qwe!@#'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalize(self):
        email = 'user_1@TEsT.cOm'
        user = get_user_model().objects.create_user(
            email=email,
            password='123qwe!@#'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='123qwe!@#'
            )
