from django.forms import ModelForm
from product.models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product

        fields = ('img', 'barcode', 'date_best_before', 'product_name',
                  'barcode', 'number_of_market')
