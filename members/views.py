from django.shortcuts import render
from .forms import MemberRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
def signup_view(request):

    if request.method == "POST":
        form = MemberRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            fName = form.cleaned_data.get("FirstName")
            messages.success(request, f"Merhaba {fName}, hesabın başarıyla oluşturuldu!")
            new_user = authenticate(
                username = form.cleaned_data["Email"],
                password = form.cleaned_data["password1"],
            )

            login(request, new_user)
            return redirect('shop:index')

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