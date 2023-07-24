from django.db import models


# Create your models here.
class Market(models.Model):
    number_market = models.PositiveIntegerField(unique=True, primary_key=True)
    adress_market = models.CharField(max_length=65,unique=True)

    def __str__(self):
        out = f'Магазин N{self.number_market}: {self.adress_market}'
        return out