from django.db import models


# Create your models here.
class Market(models.Model):
    number_market = models.CharField(max_length=15,unique=True)

    
    def __str__(self):
        return self.number_market