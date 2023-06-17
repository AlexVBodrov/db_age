from django.db import models

# Create your models here.
class User(models.Model):
    TypePosition = {
        ('M'): 'Menedger',
        ('SS'): 'senior sales',
        ('W'): 'worker'
    }
    
    name = models.CharField(max_length=50)
    position = models.Choices(max_length=5)
    telephone = models.CharField(max_length=12)
    e_mail = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
