from django.contrib import admin
from .models import Product
from .models import ProductCategory
from .models import User


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(User)
