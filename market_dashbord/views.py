import datetime
from django.shortcuts import get_object_or_404, redirect, render
from market_dashbord.forms import MarketForm
from market_dashbord.models import Market
from product.models import Product
# Create your views here.
"""
Главная-> Инструкция к приложению

если залогиниться:
    Добавить товар в базу данных
    Просмотр товара с подходящими сроками годности(6 дней)
    Просмотр товара с подходящими сроками годности(30 дней)

если Менеджер магазина:
    может списывать товар
    Личный кабинет(Управление):
        Доступ для сотрудников магазина
        выгрузки отчетов
"""
def create_new_market(request):
    if request.method == "POST":
        form = MarketForm(request.POST)
        print(request.POST)
        if form.is_valid():
            instanse = form.save(commit=False)
            instanse.save()
        return redirect('market_detail', pk=instanse.pk)
        # return render(request, 'new-market.html', {'form': form, 'title':'Create new market'})
    else:
        form = MarketForm()
        
    return render(request, 'new-market.html', {'form': form, 'title':'Create new market'})

def show_market(request, pk):
    number_market = get_object_or_404(Market, pk=pk)
    show_all_products = Product.objects.all()
    
    context= {'show_all_products': show_all_products,
              'date': datetime.datetime.now(),
              'title': 'show_market',
              'number_market': number_market}
    
    return render(request, 'market_detail.html', context)

def create_food_record(request, record):
    '''
        Create a food record
        Добавить товар в базу данных
    '''
    pass


def show_6_day_food():
    '''
        Просмотр товара с подходящими сроками годности(6 дней)
    '''
    pass


def show_30_day_food():
    '''
        Просмотр товара с подходящими сроками годности(30 дней)
    '''
    pass