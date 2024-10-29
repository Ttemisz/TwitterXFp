from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')  
        messages.error(request, 'Usuário ou senha errados')

    return render(request, 'users/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'As senha esta errada')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Esse ja cadastrado')
        else:
            User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, 'Conta criada ')
            return redirect('login')

    return render(request, 'users/register.html')
