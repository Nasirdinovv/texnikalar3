from django.shortcuts import render
from .models import Product


def all_products(request):
    products_list = Product.objects.all()
    return render(request, 'products_list.html', {'products_list': products_list})