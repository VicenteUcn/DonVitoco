from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'build.html')

def menu(request):
    return render(request, 'carta.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
