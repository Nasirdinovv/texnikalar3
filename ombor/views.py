from django.shortcuts import render
from .models import Product


def all_products(request):
    products_list = Product.objects.all()
    return render(request, 'products_list.html', {'products_list': products_list})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})