from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from .models import *


# Create your views here.
def index(request):
    context = {
        'title': 'Platform'
    }
    return render(request, 'task1/index.html', context)


def store(request):
    games = Game.objects.all()
    context = {
        'title': 'Store',
        'games': games
    }
    return render(request, 'task1/store.html', context)


def cart(request):
    context = {
        'title': 'Cart',
        'content': 'Корзина пока что пуста. Чтобы добавить товары '
                   'нажмите кнопку КУПИТЬ в магазине'
    }
    return render(request, 'task1/cart.html', context)


def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            password_rep = form.cleaned_data['password_rep']
            age = form.cleaned_data['age']

            for buyer in buyers:
                if login == buyer.name:
                    info['error'] = f'Пользователь {login} уже существует'
            if password != password_rep:
                info['error'] = 'Пароли не совпадают'
            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
            if info:
                return render(request, 'task1/register.html', context=info)
            Buyer.objects.create(name=login, password=password, age=age)
            info['error'] = f'Пользователь {login} создан'
            return render(request, 'task1/register.html', context=info)

    form = RegistrationForm()
    return render(request, 'task1/register.html',
                  {'form': form, 'title': 'Registration'})
