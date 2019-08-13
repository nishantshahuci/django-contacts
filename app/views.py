# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Homepage
def index(request):
    ''' display homepage '''
    return render(request, 'app/index.html')

# Register page
def register(request):
    ''' display register page and attempt to register user '''

    if request.user.is_authenticated:
        # if user is already logged in, redirect to contacts page
        return redirect('contacts:contacts')

    if request.method == 'POST':
        # what happens when user tries to register
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.save()

        if user and user.is_active:
            # register was successful
            login(request, user)
            return redirect('contacts:contacts')
        else:
            # register failed
            return HttpResponse('Invalid register')

    else:
        return render(request, 'app/register.html', {})

# Login page
def user_login(request):
    ''' attempt to log in a user '''

    if request.user.is_authenticated:
        # if user is already logged in, redirect to contacts page
        return redirect('contacts:contacts')

    if request.method == 'POST':
        # what happens when user tries to Login
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            # login was successful
            login(request, user)
            return redirect('contacts:contacts')
        else:
            # login failed
            return HttpResponse('Invalid login')

    else:
        return render(request, 'app/login.html', {})

@login_required
def user_logout(request):
    ''' logout user if they are logged in '''
    logout(request)
    return redirect('home')
