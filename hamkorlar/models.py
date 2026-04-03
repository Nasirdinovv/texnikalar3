from django.db import models
from ombor.models import Product

PARTNER_TYPE = [
    ('T', "Ta'minotchi"),
    ('M', "Mijoz"),
]
werwer
class Partner(models.Model):
    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    type = models.CharField(choices=PARTNER_TYPE)

class Product_in(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in')
    reciewer = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='recievers')
    amount = models.PositiveIntegerField()
    price = models.FloatField()
    date = models.DateField()

class Product_out(models.Model):
    customer = models.ForeignKey(Partner, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name='products_out')