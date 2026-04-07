from django.db import models
from ombor.models import Product

PARTNER_TYPE = [
    ('T', "Ta'minotchi"),
    ('M', "Mijoz"),
]


class Partner(models.Model):
    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    type = models.CharField(choices=PARTNER_TYPE)

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.location} "

class Product_in(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in')
    reciewer = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='recievers')
    amount = models.PositiveIntegerField()
    price = models.CharField(max_length=50)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.product} - {self.reciewer} - {self.amount} - {self.price} - {self.date}"

class Product_out(models.Model):
    customer = models.ForeignKey(Partner, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name='products_out')
    summa = models.CharField(max_length=50)
    date = models.DateField()
    price = models.CharField(max_length=50,)
    
    def __str__(self):
        return f"{self.customer} - {self.summa} - {self.date} - {self.price}"