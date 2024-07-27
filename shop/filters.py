from django_filters import FilterSet

from shop.models import Book

class BookFilter(FilterSet):
    class Meta:
        name=Book
        fields=['title','price','authors','genres'] 