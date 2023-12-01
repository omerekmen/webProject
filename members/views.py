from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from cart.models import *
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from webProject.context_processors import get_client_ip


@receiver(user_logged_in)
def update_user_ip(sender, request, user, **kwargs):
    user_ip = get_client_ip(request)  # Use the function to get the client's IP address
    user.ip_address = user_ip
    user.save()

def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Merhaba {username}, hesabın oluşturuldu")
            new_user = authenticate(username= form.cleaned_data['username'],
                                    password= form.cleaned_data['password1'])
            login(request, new_user)
            Cart.objects.get_or_create(member=request.user)
            return redirect("index")

    else:
        initial_ip = get_client_ip(request)
        form = RegisterForm(initial={'ip_address': initial_ip})

    return render(request, 'registration/register.html', {'form': form})   

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form input.")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')