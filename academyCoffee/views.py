from .models import ProductCategory, Product, Basket, User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def cart(request):
    context = {
        'title': "Корзина",
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'main/cart.html', context)


def index(request):
    context = {
        'title': "Академия кофе"
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': "О нас"
    }
    return render(request, 'main/about.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': "Личный кабинет",
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
        'user': request.user

    }
    return render(request, 'main/personalaccount.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегестрировались')
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': "Регистрация"
    }
    return render(request, 'users/register.html', context)

@login_required
def orderhistory(request):
    return render(request, 'main/orderhistory.html', {'title': "История заказов"})


def stocks(request):
    context = {
        'title': "Акции"
    }
    return render(request, 'main/stocks.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'title': "Авторизация"
    }
    return render(request, 'users/auth.html', context)


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


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required
def basket_deletion(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    basket = baskets.first()
    if basket.quantity == 1:
        basket.delete()
    else:
        basket.quantity -= 1
        basket.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META['HTTP_REFERER'])

