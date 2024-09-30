from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


class BookTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Test Book",
            subtitle="Test Sub Book",
            author="Test Author",
            isbn="123456",
        )

    def test_api_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
