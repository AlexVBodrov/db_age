from django.db import models

# Create your models here.
class Product(models.Model):
    img = models.ImageField()
    date_best_before = models.DateTimeField()
    barcode = models.CharField(max_length=15)
    product_name = models.CharField(max_length=100)
    write_off = models.BooleanField(default=False)