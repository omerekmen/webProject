from django.shortcuts import render
from .models import Products

# Create your views here.

def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})

def category(request):
    return render(request, 'category.html')

def product(request):
    return render(request, 'product.html')

def combproduct(request):
    return render(request, 'combproduct.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

