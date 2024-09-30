from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from books.models import Book

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'