from django.db import models

# Create your models here.
class Market(models.Model):
    number_market = models.IntegerField(max_length=8)
    employee = models.ForeignKey(User)
    goods = models.ForeignKey(Product)