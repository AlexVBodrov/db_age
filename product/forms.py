import datetime
from django.forms import ModelForm
from product.models import Product
from django import forms
from django.core.exceptions import ValidationError


class AddProductForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cat'].empty_label = "Категория не выбрана"
        #     self.fields['name'].widget.attrs.update({'class': 'special'})
        # self.fields['comment'].widget.attrs.update(size='40')

    class Meta:
        model = Product

        fields = ('img', 'barcode', 'date_best_before', 'product_name',
                  'barcode', 'number_of_market')

        widgets = {
            'date_best_before': forms.widgets.DateInput(attrs={'type': 'date'})}
        # 'title': forms.TextInput(attrs={'class': 'form-input'}),
        # 'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

    def clean_barcode(self):
        barcode = self.cleaned_data['barcode']
        if len(barcode) > 15:
            raise ValidationError('Длина превышает 200 символов')

        return barcode
