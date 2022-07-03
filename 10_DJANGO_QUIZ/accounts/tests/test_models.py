from django.contrib.auth.models import Group

from accounts.models import CustomUser

from django.test import TestCase


class TestModels(TestCase):
    username = None

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Users')
        cls.username = 'user_1'

        CustomUser.objects.create(
            username=cls.username,
            password='123qwe!@#',
            email='user_1@test.com'
        )

    def setUp(self) -> None:
        self.user = CustomUser.objects.get(pk=1)

    # @classmethod
    # def tearDownClass(cls):
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_avatar_label_is_correct(self):
        avatar_label = self.user._meta.get_field('avatar').verbose_name
        self.assertEqual(avatar_label, 'avatar')

    def test_city_max_length(self):
        meta = self.user._meta.get_field('city')
        self.assertEqual(meta.max_length, 50)
        self.assertTrue(meta.blank)
        self.assertTrue(meta.null)

    def test_convert_user_to_str(self):
        self.assertEqual(str(self.user), self.username)
