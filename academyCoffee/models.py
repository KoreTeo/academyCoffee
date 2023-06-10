from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


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

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class User(AbstractUser):
    regions = [
        ('Красноярск', 'Красноярск'),
        ('Москва', 'Москва'),
        ('Санкт-Петерург', 'Санкт-Петерург'),
        ('Новосибирск', 'Новосибирск'),
    ]
    region = models.TextField('Регион', max_length=50, choices=regions, blank=True)
    PNumber = models.PositiveIntegerField('Номер телефона', blank=True, null=True)
    DateOfBirth = models.DateField("День рождения", default=timezone.now)


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


