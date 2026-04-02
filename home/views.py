from django.shortcuts import render
from hr.models import Workers
from ombor.models import Product


def home_page(request):
    hodimlar_soni = Workers.objects.all().count()
    mahsulotlar_soni = Product.objects.all().count()

    return render(request, 'index.html', {'hodimlar_soni': hodimlar_soni, 'mahsulotlar_soni': mahsulotlar_soni})