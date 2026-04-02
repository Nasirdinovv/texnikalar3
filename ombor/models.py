from django.db import models

UNITS = [
    ('l', "Lits"),
    ('piece', "Dona"),
    ('box', "Quti"),
]

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/image', blank=True, null=True )
    category = models.ManyToManyField(to='Category', related_name='products')
    unit = models.CharField(choices=UNITS, default='pieace')
    amount = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=25)