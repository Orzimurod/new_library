from django.db import models
from django.contrib.auth import get_user_model

class Genre(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Author(models.Model):
    name=models.CharField(max_length=200)
    birth_date=models.DateField()
    country=models.CharField
    picture=models.ImageField(upload_to='authors')

    
    def __str__(self):
        return self.name

class Book(models.Model):
    COVER_CHOICES=(
        ('hard', 'Qattiq muqova'),
        ('soft', 'Yumshoq muqova'),
    )
    title=models.CharField(max_length=500)
    authors=models.ManyToManyField(Author)
    pages=models.IntegerField(default=0)
    genres=models.ManyToManyField(Genre)
    date_published=models.DateField()
    description=models.TextField(blank=True, null=True)
    language=models.CharField(max_length=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField(default=10)
    image=models.ImageField(upload_to='books')
    paper_format=models.CharField(max_length=2)
    cover=models.CharField(choices=COVER_CHOICES,default=COVER_CHOICES[0][0],max_length=4)
    on_trend=models.BooleanField(default=False)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,blank=True,null=True)

    

    def __str__(self):
        return self.title
    

    