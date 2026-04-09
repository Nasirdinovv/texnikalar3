from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def all_products(request):
    products_list = Product.objects.all()
    return render(request, 'products_list.html', {'products_list': products_list})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id) 
    product.delete()
    return redirect('all_products')

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        name = request.POST.get("name")
        image = request.POST.get("image")
        unit = request.POST.get("unit")
        amount = request.POST.get("amount")
        
        product.name = name
        product.image = image
        product.unit = unit
        product.amount = amount
        
        product.save()
        return redirect('product_detail', id)
        
        
    elif request.method == 'GET':
        return render(request, 'product_update.html', {'product': product})
    return redirect('all_products')
    

        