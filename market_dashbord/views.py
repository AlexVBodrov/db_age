import datetime
from django.shortcuts import get_object_or_404, redirect, render
from market_dashbord.forms import MarketForm, ChooseMarketForm
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
        if form.is_valid():
            instanse = form.save(commit=False)
            instanse.save()
        return redirect('market_dashbord:market_detail', pk=instanse.number_market)
    else:
        form = MarketForm()
        
    return render(request, 'new-market.html', {'form': form, 'title':'Create new market'})

def show_market(request, pk):
    number_market = get_object_or_404(Market, pk=pk)
    show_all_products = Product.objects.filter(number_of_market=number_market)
    
    context= {'show_all_products': show_all_products,
              'date': datetime.datetime.now(),
              'title': 'show_market',
              'number_market': number_market}
    
    return render(request, 'market_detail.html', context)

def show_all_markets(request):
    all_markets = Market.objects.all()
    
    context= {'all_markets': all_markets,
              'date': datetime.datetime.now(),
              'title': 'show_market'}
    
    return render(request, 'show_all_markets.html', context)

def show_my_market(request):
    """ выбрать магазин"""
    
    if request.method == 'POST':
        number_market = request.POST.get('number_market')
        return redirect('market_dashbord:market_detail', pk=number_market)
    else:
        form = ChooseMarketForm(request.POST)
    return render(request, 'show_my_market.html', {'form': form, 'title':'show_my_market'})
    

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

def show_contacts(request):
    return render(request, 'contact.html')