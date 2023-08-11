import datetime
from django.shortcuts import render
from product.models import Product

# Create your views here.


def show_main_page(request):
    show_all_products = Product.objects.all()

    context = {'show_all_products': show_all_products,
               'date': datetime.datetime.now(),
               'title': 'Главная страница'}

    return render(request, 'index.html', context=context)
