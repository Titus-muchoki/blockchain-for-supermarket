from django.contrib import admin

from products.models import Product, Sale

# Register your models here.
admin.site.register(Product)
admin.site.register(Sale)