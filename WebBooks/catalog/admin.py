from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance


class ModelAdmin(admin.ModelAdmin):
    pass
# определение к классу администратор
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
# Поля редактирования даты по горизонтали, exclude нужен для того, чтоб убрать поля, которые не нужно отображать
    fields = ['first_name', 'last_name',
              ('date_of_birth', 'date_of_death')]
    pass


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Регистрируем классы администратора для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]

# Регистрируем классы администратора для экземпляра книги
@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
