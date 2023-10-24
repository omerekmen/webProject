from django.shortcuts import render
from products.models import *
from products.views import *
from datetime import datetime, timedelta


# Functions to Manage Products
products = Products.objects.all()

def one_month_ago():
    today = datetime.now().date()
    return today - timedelta(days=30)

# Create your views here.

def index(request):
    return render(request, 'index.html', {'products': products, 'one_month_ago': one_month_ago()})

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

