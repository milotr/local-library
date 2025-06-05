from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.http import request

# Create your views here
def index(request):
    '''View function for hame page of site.'''

    # generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
    }

    return render(request, 'index.html', context=context)