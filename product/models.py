from django.db import models
from market_dashbord.models import Market

# Create your models here.


class Product(models.Model):
    img = models.ImageField(
        upload_to='products/%Y-%m-%d/', verbose_name='Product')
    date_best_before = models.DateField()
    barcode = models.CharField(max_length=15, blank=True)
    product_name = models.CharField(max_length=100, blank=True)
    write_off = models.BooleanField(default=False)
    number_of_market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['date_best_before']
