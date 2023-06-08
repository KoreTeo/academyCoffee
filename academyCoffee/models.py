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
    PNumber = models.PositiveIntegerField('Номер телефона')
    DateOfBirth = models.DateField("День рождения", default=timezone.now)
