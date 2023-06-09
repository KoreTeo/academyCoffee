from django.shortcuts import render, redirect
from .models import ProductCategory, Product
from academyCoffee.models import User
from academyCoffee.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse


def cart(request):
    return render(request, 'main/cart.html', {'title': "Корзина"})


def index(request):
    return render(request, 'main/index.html', {'title': "Академия кофе"})


def about(request):
    return render(request, 'main/about.html', {'title': "О нас"})


def profile(request):
    return render(request, 'users/profile.html', {'title': "Личный кабинет"})


def profile2(request):
    return render(request, 'main/personalaccount.html', {'title': "Личный кабинет"})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'title': "Авторизация"
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    form = UserRegistrationForm()
    context = {
        'form': form,
        'title': "Регистрация"
    }
    return render(request, 'users/register.html',context)


def orderhistory(request):
    return render(request, 'main/orderhistory.html', {'title': "История заказов"})


def stocks(request):
    return render(request, 'main/stocks.html', {'title': "Акции"})


def menu(request):
    context = {
        'title': "Меню",
        'products': Product.objects.all(),
        'productsWithCategory1': Product.objects.filter(category__name="СЕЗОННЫЕ НАПИТКИ"),
        'productsWithCategory2': Product.objects.filter(category__name="ГОРЯЧИЕ НАПИТКИ"),
        'productsWithCategory3': Product.objects.filter(category__name="ХОЛОДНЫЕ НАПИТКИ"),
        'productsWithCategory4': Product.objects.filter(category__name="АВТОРСКИЕ НАПИТКИ"),
        'productsWithCategory5': Product.objects.filter(category__name="К КОФЕ"),
        'productsWithCategory6': Product.objects.filter(category__name="НАША КУХНЯ"),

    }
    return render(request, 'main/menu.html', context)


