from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserEditForm
from market_dashbord.models import Market
from product.models import Product
from users.models import User

from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'вход'
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            # чтобы переходил на свой магазин по ID
            try:
                number_market = User.objects.get(username=username).market_number.number_market
                return redirect('market_dashbord:market_detail', pk=number_market)
            except:
                return HttpResponseRedirect(reverse('main_page'))
    content = {'title': title, 'login_form': login_form}
    return render(request, 'users/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main_page'))


def edit(request):
    title = 'редактирование'
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES,
                                 instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('users:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'users/edit.html', content)


def register(request):
    # create a new user
    title = 'регистрация'
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        register_form = UserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'users/register.html', content)
