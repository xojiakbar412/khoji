from django.http import HttpResponse
from django.shortcuts import render
from uuid import uuid4
from product.models import Product


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'product/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product/product_detail.html', context)
