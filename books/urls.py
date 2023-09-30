from django.urls import path
from .views import list_books, create_book, delete_book, edit_book

urlpatterns = [
    path('', list_books),
    path('new/', create_book, name='create_book'),
    path('edit/<int:id>/', edit_book, name='edit_book'),
    path('delete/<int:id>/', delete_book, name='delete_book')
]