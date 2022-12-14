from email import message
import imp
from re import U
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request, './user/profile.html')


def user_login(request):
    message, username = '', ''
    if request.method == 'POST':
        if request.POST.get('login'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            print(username, password)

            if username == '' or password == '':
                message = '帳號密碼不能為空'
            else:
                user = authenticate(
                    request, username=username, password=password)
                if user is None:
                    if User.objects.filter(username=username):
                        message = '密碼有誤'
                    else:
                        message = '帳號有誤'
                else:
                    login(request, user)
                    message = '登入中.....'
                    return redirect('todo')

        elif request.POST.get('register'):
            return redirect('register')

    return render(request, './user/login.html', {'message': message, 'username': username})


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
                user = User.objects.create_user(
                    username=username, password=password1)
                user.save()
                message = '註冊成功'
                login(request, user)
                return redirect('profile')

    return render(request, './user/register.html', {'form': form, 'message': message})
