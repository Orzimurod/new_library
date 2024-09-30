from django import forms
from shop.models import Book
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'name', 'phone_number', 'address', 'city']


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
