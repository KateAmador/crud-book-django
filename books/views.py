from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import BookFilterForm, BookForm

# Create your views here.
def create_book(request):
    book = Book(title=request.POST['title'],
                author=request.POST['author'],
                category=request.POST['category'])
    book.save()
    return redirect('/books/')

def list_books(request):
    books = Book.objects.all()
    filter_form = BookFilterForm(request.GET)

    if filter_form.is_valid():
        category = filter_form.cleaned_data.get('category')
        author = filter_form.cleaned_data.get('author')

        if category:
            books = books.filter(category=category)
        if author:
            books = books.filter(author__icontains=author)

    return render(request, 'list_books.html', {'books': books, 'filter_form': filter_form})

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})

def delete_book(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect('/books/')