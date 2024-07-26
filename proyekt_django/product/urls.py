from django.contrib import admin
from django.urls import path
from product.views import product_list, product_detail

urlpatterns = [
    path('product-list/',product_list, name='products_list'),
    path('product-detail/<int:product_id>', product_detail, name='product_detail')
]