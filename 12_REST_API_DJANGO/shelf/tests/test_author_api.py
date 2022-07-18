from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Author
from ..serializers import AuthorSerializer

AUTHOR_LIST_URL = reverse('shelf:author-list')
AUTHOR_ADD_URL = reverse('shelf:author-add')


def detail_url(author_id):
    return reverse('shelf:author-detail', args=[author_id])


def sample_author(name='Артур Кларк', country='США'):
    return Author.objects.create(name=name, country=country)


class PublicAuthorApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_retrieve_author_list(self):
        Author.objects.create(
            name='Джордж Оруэлл',
            country='Англия'
        )

        Author.objects.create(
            name='Тарас Шевченко',
            country='Украина'
        )

        response = self.client.get(AUTHOR_LIST_URL)

        authors = Author.objects.all().order_by('name')
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_author_create_login_required(self):
        response = self.client.get(AUTHOR_ADD_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_author_detail_login_required(self):
        url = reverse('shelf:author-detail', args=[1])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateAuthorApiTests(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user_1@test.com'
            '123qwe!@#'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_author_successful(self):
        payload = {
            'name': 'Джордж Оруэлл',
            'country': 'Англия'
        }
        response = self.client.post(AUTHOR_ADD_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = Author.objects.filter(
            name=payload['name']
        ).exists()

        self.assertTrue(exists)

    def test_create_author_invalid(self):
        payload = {
            'name': '',
            'country': 'Англия'
        }
        response = self.client.post(AUTHOR_ADD_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_author(self):
        author = sample_author()

        payload = {
            'name': 'Фрэнк Герберт'
        }
        url = detail_url(author.id)

        self.client.put(url, payload)
        author.refresh_from_db()
        self.assertEqual(author.name, payload['name'])

    def test_full_update_author(self):
        author = sample_author()

        payload = {
            'name': 'Джордж Оруэлл',
            'country': 'Англия'
        }
        url = detail_url(author.id)

        self.client.put(url, payload)
        author.refresh_from_db()
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(author, key))

    def test_remove_author(self):
        author = sample_author()
        url = detail_url(author.id)
        self.client.delete(url)

        exists = Author.objects.filter(
            id=author.id
        ).exists()

        self.assertFalse(exists)
