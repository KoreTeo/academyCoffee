from django.contrib import admin

from .models import Basket, Order, Product, ProductCategory, User, Promocode

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(User)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(Promocode)
