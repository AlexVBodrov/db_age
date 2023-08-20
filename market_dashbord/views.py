import datetime
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse
from market_dashbord.forms import MarketForm, ChooseMarketForm
from market_dashbord.models import Market
from product.forms import AddProductForm
from market_dashbord.models import Market
from product.models import Product
from users.models import User
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

    return render(request, 'new-market.html', {'form': form, 'title': 'Create new market'})


def show_market(request, pk):
    number_market = get_object_or_404(Market, pk=pk)
    show_all_products = Product.objects.filter(number_of_market=number_market)

    context = {'show_all_products': show_all_products,
               'date': datetime.datetime.now(),
               'title': 'show_market',
               'number_market': number_market}

    return render(request, 'market_detail.html', context)


def show_all_markets(request):
    all_markets = Market.objects.all()

    context = {'all_markets': all_markets,
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
    return render(request, 'show_my_market.html', {'form': form, 'title': 'show_my_market'})


def create_food_record(request):
    '''
        Create a food record
        Добавить товар в базу данных
    '''
    title = 'Добавить товар в базу данных'

    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            instanse = form.save(commit=False)
            instanse.save()
        number_market = request.POST.get('number_of_market')
        return redirect('market_dashbord:market_detail', pk=number_market)
    else:
        form = AddProductForm()

    return render(request, 'create_food_record.html', {'form': form, 'title': title})


def show_6_day_food(request):
    '''
        Просмотр товара с подходящими сроками годности(6 дней)
    '''

    if request.user.is_authenticated:
        num_market = request.user.market_number

        products = Product.show_date_best_before(num_market, 6).filter(write_off=False)
        for product in products:
            product.expired()

        context = {'all_items': products,
                   'date': datetime.datetime.now(),
                   'title': 'show_6_day_best_before',
                   'number_market': num_market}
        return render(request, 'show_6_day_best_before.html', context)
    else:
        return HttpResponseRedirect(reverse('main_page'))


def show_30_day_food(request):
    '''
        Просмотр товара с подходящими сроками годности(30 дней)
    '''
    num_market = request.user.market_number

    products = Product.show_date_best_before(num_market, 30).filter(write_off=False)
    for product in products:
        product.expired()

    context = {'all_items': products,
               'date': datetime.datetime.now(),
               'title': 'show_6_day_best_before'}
    return render(request, 'show_30_day_best_before.html', context)


def show_write_off(request):
    '''
        Просмотр списсанного товара(30 дней)
    '''
    num_market = request.user.market_number

    products = Product.show_date_best_before(num_market, 30).filter(write_off=True)

    context = {'all_items': products,
               'date': datetime.datetime.now(),
               'title': 'show_6_day_best_before'}
    return render(request, 'show_write_off.html', context)

def show_contacts(request):
    return render(request, 'contact.html')


def write_off_product(request, pk):
    product =  get_object_or_404(Product, pk=pk)
    product.write_off = True
    product.save()
    return redirect('market_dashbord:show_6_day_food')