from django.urls import path
from .views import all_products, product_detail, delete_product, update_product

urlpatterns = [
    path('', all_products, name='all_products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path('uptade/delete/<int:id>/', update_product, name='update_product'),
    
]
