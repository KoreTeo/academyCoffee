import requests
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    stars = models.DecimalField(max_digits=5, decimal_places=1)
    image = models.ImageField(upload_to='products_images')
    category = models.ManyToManyField(ProductCategory)

    def __str__(self):
        return self.name

    def product_in_basket(self):
        if Basket.objects.filter().contains(Product):
            return True
        else:
            return False

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class User(AbstractUser):
    regions = [
        ('Красноярск', 'Красноярск'),
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Новосибирск', 'Новосибирск'),
    ]
    username = models.CharField(unique=False, blank=True, null=True, max_length=20)
    region = models.TextField('Регион', max_length=50, choices=regions, blank=True)
    PNumber = PhoneNumberField('Номер телефона', blank=False, null=False, unique=True, region="RU")
    DateOfBirth = models.DateField("День рождения", default=timezone.now)
    payment_method = models.CharField('Способ оплаты', max_length=20, default='Наличные')

    USERNAME_FIELD = "PNumber"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f'Имя: {self.first_name} | Email: {self.email} | Номер телефона: {str(self.PNumber)}'


class UserCard(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    is_base = models.BooleanField(default=False)
    number = models.DecimalField(max_digits=16, decimal_places=0)
    month = models.DecimalField(max_digits=2, decimal_places=0)
    year = models.DecimalField(max_digits=2, decimal_places=0)
    CVCCode = models.DecimalField(max_digits=3, decimal_places=0)

    def protect_number(self):
        return int(str(self.number)[-4:])

    def first_number(self):
        return int(str(self.number)[:1])

    def base_card(self):
        return UserCard.objects.get(user=self.user, is_base=1).protect_number()


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum())
        }
        return basket_item

    def product_in_basket(self):
        if Basket.objects.filter(user=self.user).contains(self.product):
            return True
        else:
            return False


class Order(models.Model):
    CREATED = 0
    COOKING = 1
    PREPARED = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Обработка'),
        (COOKING, 'Готовим'),
        (PREPARED, 'Можно забирать'),
        (DELIVERED, 'Доставлен'),
    )

    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    serving = models.CharField('Сервировка', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    payment_method = models.CharField('Способ оплаты', max_length=20)
    promocode_name = models.CharField('Промокод', max_length=20, blank=True, null=True)

    def __str__(self):
        return f'Заказ для {self.user}'


class Promocode(models.Model):
    name = models.CharField('Промокод', max_length=20)
    stock = models.PositiveSmallIntegerField(default=25)


class EmailSubscribe(models.Model):
    email = models.CharField('Почта', max_length=50)


class OfferForCooperation(models.Model):
    subject = models.CharField(max_length=50)
    name = models.CharField('Имя', max_length=15)
    regions = [
        ('Красноярск', 'Красноярск'),
        ('Москва', 'Москва'),
        ('Санкт-Петерург', 'Санкт-Петерург'),
        ('Новосибирск', 'Новосибирск'),
    ]
    region = models.TextField('Регион', max_length=50, choices=regions, blank=True)
    text = models.TextField()
    email = models.EmailField('Почта', max_length=50)
