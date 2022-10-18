from email import message
import imp
from re import U
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_login(request):
    return render(request, './user/login.html')


def user_register(request):

    form = UserCreationForm()
    message = ''

    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(password1) < 8:
            message = '密碼少於8各字元'
        elif password1 != password2:
            message = '兩次密碼不同'
        else:
            if User.objects.filter(username=username).exists():
                message = '帳號重複'
            else:
                User.objects.create_user(
                    username=username, password=password1).save()
                message = '註冊成功'

    return render(request, './user/register.html', {'form': form, 'message': message})
