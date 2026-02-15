# views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import *  # Import book model
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_all_books(request):
    # Get all books from the database
    all_books = Book.objects.all()
    
    # Create a context dictionary to pass data to the template
    context = {
        'books': all_books,  # This will be available in the template as 'books'
    }
    
    # Render the template with the context data
    return render(request, 'view_all_books.html', context)

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, 'single_book.html', {'book':single_book})