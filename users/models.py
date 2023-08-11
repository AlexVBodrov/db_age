from django.db import models
from market_dashbord.models import Market


# Create your models here.
class User(models.Model):
    TYPE_POSITION = (
        ('M', 'Manager'),
        ('SS', 'senior sales'),
        ('W', 'worker'),
    )

    name = models.CharField(max_length=25)
    position = models.CharField(max_length=2, choices=TYPE_POSITION)
    telephone = models.CharField(max_length=12)
    e_mail = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=20)
    number_market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
