import datetime
from django.forms import ModelForm
from product.models import Product
from django import forms
from django.core.exceptions import ValidationError


class AddProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


    class Meta:
        model = Product

        fields = ('img', 'barcode', 'date_best_before', 'product_name',
                  'barcode', 'number_of_market')

        widgets = {
            'img': forms.widgets.FileInput(attrs={'class': "form-control",}),
            'date_best_before': forms.widgets.DateInput(attrs={'class': "form-control", 'type': 'date'}),
            'number_of_market': forms.widgets.Select(attrs={'readonly':'readonly', 'disabled': 'disabled'}),
            
            }
        # 'title': forms.TextInput(attrs={'class': 'form-input'}),
        # 'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        #         widgets = {
        #     'name': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     'email': EmailInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Email'
        #         })
        # }

            # field_name['number_of_market'].widget.attrs['readonly'] = True
    #     self.fields['name'].widget.attrs.update({'class': 'special'})
    # self.fields['comment'].widget.attrs.update(size='40')

    def clean_barcode(self):
        barcode = self.cleaned_data['barcode']
        if len(barcode) > 15:
            raise ValidationError('Длина превышает 15 символов')

        return barcode
