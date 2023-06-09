from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookInstance, Author, Genre


def index(request):
    # Генерация количеств некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступные книги (статус = 'На складе')
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_available = BookInstance.objects.filter(status_exact=2).count()

    # Авторы книг,
    num_authors = Author.objects.count()

    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной context
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors,
                           },
                  )
