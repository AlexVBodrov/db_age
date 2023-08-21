from django.db import models
import datetime
from market_dashbord.models import Market

# Create your models here.


class Product(models.Model):
    img = models.ImageField(
        upload_to='products/%Y-%m-%d/', verbose_name='Фото продукта')
    date_best_before = models.DateField(verbose_name='Годен до какого числа')
    barcode = models.CharField(max_length=15, blank=True, verbose_name='Штрихкод')
    product_name = models.CharField(max_length=100, blank=True, verbose_name='Название')
    write_off = models.BooleanField(default=False, verbose_name='Списан')
    is_expired = models.BooleanField(default=False, verbose_name='Просрочен')
    number_of_market = models.ForeignKey(Market, on_delete=models.CASCADE, verbose_name='Магазин')

    def __str__(self):
        return self.product_name

    @staticmethod
    def show_date_best_before(num_market, days):
        if days > 31:
            days = 31
        startdate = datetime.date.today()
        enddate = startdate + datetime.timedelta(days=days)
        show_products_best_before = Product.objects.filter(number_of_market=num_market).filter(
            date_best_before__range=[startdate, enddate])
        return show_products_best_before

    def expired(self):
        # Меняет статус на просроченный
        today_date = datetime.date.today()
        if self.date_best_before <= today_date:
            self.is_expired = True


    class Meta:
        ordering = ['date_best_before']
