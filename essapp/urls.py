
from django.urls import path
from .views import *

urlpatterns = [
    path('friends', show_friends),
    path('product', show_product),
    path('product-details/<id>', product_details, name='product-detail'),
    path('add-product', add_product, name='add-product')
]
