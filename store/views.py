from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render
from products.models import *
from products.views import *
from members.urls import *
from datetime import datetime, timedelta


# Functions to Manage Products
active_products = Products.objects.filter(product_state='Aktif')

# Create your views here.
def index(request):
    return render(request, 'index.html', {'active_products': active_products})


def category(request):
    return render(request, 'category.html')

def product(request):
    return render(request, 'product.html')

def combproduct(request):
    return render(request, 'combproduct.html')

