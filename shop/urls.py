from django.urls import path
from .views import index_view,ShopView,book_details,about_view,contact_view,login_view,register_view,BookCreateView,logout_view

urlpatterns=[
    path('',index_view,name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('book/<int:pk>/', book_details, name='book_details'),
    path('about', about_view, name='about'),
    path('contact',contact_view, name='contact'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register',register_view, name='register'),
    path('bookcreate',BookCreateView.as_view(), name='book-create')
    
]

