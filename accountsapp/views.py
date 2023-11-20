from django.shortcuts import render
from django.http import HttpResponse


def profile_page(request, username):
    return HttpResponse(f"Hello, it`s page for user {username} profile")

def set_password_page(request):
    return HttpResponse(f"Hello, it`s page for user set_password")

def set_userdata_page(request):
    return HttpResponse(f"Hello, it`s page for user set_userdata")

def deactivate_account_page(request):
    return HttpResponse(f"Hello, it`s page for user deactivate")

def register_account_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

def logout_page(request):
    return render(request, 'logout.html')