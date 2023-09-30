from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category']

class BookFilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'Todas'),  
        ('Fantasia', 'Fantasia'),
        ('Ficcion', 'Ficcion'),
        ('Distopico', 'Distopico'),
        ('Drama', 'Drama'),
    ]
    category = forms.ChoiceField(choices=[('', 'Todas')] + CATEGORY_CHOICES, required=False)
    author = forms.CharField(max_length=255, required=False)