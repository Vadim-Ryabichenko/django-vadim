from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import AuthenticationForm
from .forms import UserRegistrationForm


def profile_page(request, username):
    return HttpResponse(f"Hello, it`s page for user {username} profile")

def set_password_page(request):
    return HttpResponse(f"Hello, it`s page for user set_password")

def set_userdata_page(request):
    return HttpResponse(f"Hello, it`s page for user set_userdata")

def deactivate_account_page(request):
    return HttpResponse(f"Hello, it`s page for user deactivate")

def register_account_page(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/accounts/login/')
def logout_page(request):
    logout(request)
    return render(request, 'logout.html')