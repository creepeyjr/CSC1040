# views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import *  # Import book model
from django.shortcuts import get_object_or_404
from .forms import BookForm  # Import book form


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

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')  # Use your book list URL name
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

'''
def add_author(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')  # Use your book list URL name
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

# Add this new view
def add_author(request):
    if request.method == 'POST':
        # If the form was submitted, process the data
        form = AuthorForm(request.POST)
        if form.is_valid():
            # Save the new author to the database
            form.save()
            # Redirect to a success page (like the author list or home)
            return redirect('view_all_books')  # Or create an author list page later
    else:
        # If it's a GET request, show an empty form
        form = AuthorForm()
    
    # Render the form template
    return render(request, 'add_author.html', {'form': form})
'''

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'templates/registration/register.html', {'form': form})