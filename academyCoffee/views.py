from django.shortcuts import render, redirect
from .models import ProductCategory, Product


def cart(request):
    return render(request, 'main/cart.html', {'title': "Корзина"})


def index(request):
    return render(request, 'main/index.html', {'title': "Академия кофе"})


def about(request):
    return render(request, 'main/about.html', {'title': "О нас"})


def personalaccount(request):
    return render(request, 'main/personalaccount.html', {'title': "Личный кабинет"})


def stocks(request):
    return render(request, 'main/stocks.html', {'title': "Акции"})


def menu(request):
    context = {
        'title': "Меню",
        'products': Product.objects.all(),
        'productsWithCategory1': Product.objects.filter(category__name="Сезонные напитки"),
        'productsWithCategory2': Product.objects.filter(category__name="Горячие напитки"),
        'productsWithCategory3': Product.objects.filter(category__name="Холодные напитки"),
        'productsWithCategory4': Product.objects.filter(category__name="АВТОРСКИЕ НАПИТКИ"),
        'productsWithCategory5': Product.objects.filter(category__name="К КОФЕ"),
        'productsWithCategory6': Product.objects.filter(category__name="НАША КУХНЯ"),

    }
    return render(request, 'main/menu.html', context)


