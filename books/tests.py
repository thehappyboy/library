from django.test import TestCase
from django.urls import reverse
from books.models import Book

class BookModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Test Book',
            subtitle='Test Sub Book',
            author='Test Author',
            isbn='1234567890123',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.subtitle, 'Test Sub Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        self.assertTemplateUsed(response, 'books/book_list.html')
