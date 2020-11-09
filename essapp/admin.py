from django.contrib import admin

# Register your models here.
from .models import Friends, Product, Category

admin.site.register(Friends)
admin.site.register(Product)
admin.site.register(Category)