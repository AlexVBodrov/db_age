from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserEditForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    title = 'вход'
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            # добавить функцию чтобы переходил на свой магазин по ID 
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
