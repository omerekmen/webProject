from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from .forms import MemberRegisterForm
from .models import *


# Create your views here.
def signup_view(request):

    if request.method == "POST":
        form = MemberRegisterForm(request.POST)
        if form.is_valid():
            new_user = Members.objects.create_user(
                Identification = form.cleaned_data["Email"],
                PhoneNumber = form.cleaned_data["PhoneNumber"],
                FirstName = form.cleaned_data["FirstName"],
                LastName = form.cleaned_data["LastName"],
                BirthDate = form.cleaned_data["BirthDate"],
                CampusID = form.cleaned_data["CampusID"],
                Gender = form.cleaned_data["Gender"],
                LevelID = form.cleaned_data["LevelID"],
                ClassID = form.cleaned_data["ClassID"],
                RegistrationState = form.cleaned_data["RegistrationState"],
                PasswordHash = make_password(form.cleaned_data["password1"]),
            )
            new_user.save()
            login(request, new_user)
            return redirect('store:index')

    else:
        form = MemberRegisterForm()

    context = {
        'form' : form,
    }

    return render(request, 'signup.html', context=context) 


def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')