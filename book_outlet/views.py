from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book 

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        'books': books # key to be used in template DTL syntax
    })


def book_detail(request, id):
    # you can handle not found errors with try, except or easier w/get_or_404
    # try:
    #     book = Book.objects.get(id=id) # get the book that matches the id in the request
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
    })