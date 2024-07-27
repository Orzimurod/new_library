
from django.shortcuts import redirect, render
from shop.models import Book
from orders.forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import telegram
bot=telegram.Bot(token='7344642601:AAGEK5H9TmVKtl8Ves_0UnRW0F38klkBk2U')

@login_required(login_url='login')
def new_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            bot.sendMessage( 1294428161, f'Yangi zakaz {form.cleaned_data.get('phone_number')}')
        else:
            print(form.errors)

    else:
        print('get request keldi')
    return redirect('home')


 


