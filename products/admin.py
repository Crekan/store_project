from django.contrib import admin

from .models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Basket)
