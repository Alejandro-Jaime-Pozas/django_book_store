from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg #, Max, Min, Sum, Count 

from .models import Book 

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('title') # can order by any field, '-' does desc order vs asc order
    num_books = books.count() # is included with django automatically
    avg_rating = books.aggregate(Avg('rating')) # need to import from django.db.models Avg; this returns a dictionary, not an int/str
    return render(request, 'book_outlet/index.html', {
        'books': books, # key to be used in template DTL syntax
        'total_number_of_books': num_books,
        'average_rating': avg_rating
    })


def book_detail(request, slug):
    # you can handle not found errors with try, except or easier w/get_or_404
    # try:
    #     book = Book.objects.get(slug=slug) # get the book that matches the id in the request
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
    })