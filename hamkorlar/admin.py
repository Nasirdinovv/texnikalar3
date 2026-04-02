from django.contrib import admin
from .models import Partner, Product_in, Product_out

admin.site.register(Partner)
admin.site.register(Product_in)
admin.site.register(Product_out)
