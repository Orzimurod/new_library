from django.shortcuts import render, redirect
from shop.models import Book, Genre
from orders.forms import OrderForm, BookCreateForm
from django.db.models import Count
from django_filters.views import FilterView
from shop.filters import BookFilter
from django.views.generic import CreateView
from django.contrib.auth import logout


def index_view(request):
    books_on_trend = Book.objects.filter(on_trend=True)
    top_books = Book.objects.all().annotate(
           order_count=Count('Order')
      ).order_by('order_count')
    genres = Genre.objects.all()
    context = {'on_trend': books_on_trend, 'top_books': top_books, 'genres': genres}
    return render(request, 'index.html', context)


def form_valid(self, form):
    form.instance.user = self.request.user
    print(self.request.user)
    form.save()
    return redirect('books')


def book_details(request, pk):
    book = Book.objects.get(id=pk)
    form = OrderForm(initial={'book': book})
    field = form.fields['book']
    field.widget = field.hidden_widget()
    return render(request, 'book_details.html', {'book': book, 'form': form})


class ShopView(FilterView):
    model = Book
    context_object_name = 'books'
    template_name = 'shop.html'
    filterset_class = BookFilter
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__contains=search)
            return qs


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    return render(request, 'register.html')


class BookCreateView(CreateView):
    model = Book
    template_name = 'book-create.html'
    form_class = BookCreateForm
    permission_required = 'shop.add_book'

    def post(self, request, *args, **kwargs):
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('book-create')
