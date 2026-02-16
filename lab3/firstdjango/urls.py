
# django app folder urls
# firstdjango/urls.py NOT myproject/urls.py
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('books', view_all_books, name='all_books'),
    path('books/add/', views.add_book, name='add_book'),
    # path('authors/add/', views.author_book, name='author_book'),
    path('register/', views.register, name='register'),
    path('books/<int:bookid>', view_single_book, name='single_book')
]