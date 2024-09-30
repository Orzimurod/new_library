from django.db import models

from shop.models import Book


class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi buyurtma'),
        ('ready', 'Dostavkaga tayyor'),
        ('waiting', 'Yetkazilmoqda'),
        ('delivered', 'Yetkazildi'),
        ('cancelled', 'Bekor qilindi'),
    )

    CITIES = (
        ('Viloyatni tanlang', 'Viloyatni tanlang'),
        ('tashkent', 'Toshkent shahar'),
        ('andijon', 'Andijon viloyati'),
        ('buxoro', 'Buxoro viloyati'),
        ('fargona', 'Fargʻona viloyati'),
        ('jizzax', 'Jizzax viloyati'),
        ('namangan', 'Namangan viloyati'),
        ('navoiy', 'Navoiy viloyati'),
        ('qashqadaryo', 'Qashqadaryo viloyati'),
        ('qoraqalpogiston', 'Qoraqalpogʻiston Respublika'),
        ('samarqand', 'Samarqand viloyati'),
        ('sirdaryo', 'Sirdaryo viloyati'),
        ('surxondaryo', 'Surxondaryo viloyati'),
        ('toshkent', 'Toshkent viloyati'),
        ('xorazm', 'Xorazm viloyati')
    )

    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True, related_name='Order')
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=17, choices=CITIES)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
