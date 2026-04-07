from django.db import models
from django.utils import timezone


MONTHS = (
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

class Workers(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=40)
    profession = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} "

class Salary(models.Model):
    worker = models.ForeignKey('Workers', on_delete=models.CASCADE)
    month = models.CharField(max_length=25, choices=MONTHS, default="1")
    salary_sum = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.worker}"