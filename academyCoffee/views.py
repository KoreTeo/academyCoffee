from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.conf import settings
from academyCoffee.common.views import TitleMixin
from http import HTTPStatus
from .forms import UserLoginForm, UserProfileForm, UserRegistrationForm, OrderForm, CreateUserCardForm
from .models import Basket, Product, User, Order
import stripe
from django.db.models.functions import TruncMonth

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Store - Спасибо за заказ!'


class CanceledTemplateView(TemplateView):
    template_name = 'orders/canceled.html'


class OrderCreateView(TitleMixin, CreateView):
    model = Order
    template_name = 'main/cart.html'
    title = 'Корзина'
    form_class = OrderForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        baskets = Basket.objects.filter(user=self.request.user)
        form.instance.basket_history = {
            'purchase_products': [basket.de_json() for basket in baskets],
            'total_sum': float(sum(basket.sum() for basket in baskets))
        }
        baskets.delete()
        form.instance.user = self.request.user
        return super(OrderCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class OrderListView(TitleMixin, ListView):
    template_name = 'main/orderhistory.html'
    title = 'История заказов'
    queryset = Order.objects.all()
    dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data()
        context['dates'] = self.dates
        context['orderdates'] = Order.objects.filter(user=self.request.user).annotate(
            month=TruncMonth('created')).values('month').distinct()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'main/index.html'
    title = 'Академия кофе'


def about(request):
    context = {
        'title': "О нас"
    }
    return render(request, 'main/about.html', context)


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'main/personalaccount.html'
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['user'] = self.request.user
        return context


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    success_message = "Вы успешно зарегестрированы!"
    title = 'Регистрация'


@login_required
def orderhistory(request):
    return render(request, 'main/orderhistory.html', {'title': "История заказов"})


def stocks(request):
    context = {
        'title': "Акции"
    }
    return render(request, 'main/stocks.html', context)


class CreateUserCardView(TitleMixin, CreateView):
    template_name = 'main/addcart.html'
    title = 'Добавление новой карты'
    form_class = CreateUserCardForm

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateUserCardView, self).form_valid(form)


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/auth.html'
    form_class = UserLoginForm
    title = 'Авторизация'


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
