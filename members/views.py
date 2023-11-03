from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Merhaba {username}, hesabın oluşturuldu")
            new_user = authenticate(username= form.cleaned_data['username'],
                                    password= form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("index")

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})   

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})   
