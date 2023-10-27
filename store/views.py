from django.views import generic
from django.shortcuts import render
from products.models import *
from products.views import *
from datetime import datetime, timedelta


# Functions to Manage Products
products = Products.objects.all()
active_products = Products.objects.filter(product_state='Aktif')

# Create your views here.

def index(request):
    return render(request, 'index.html', {'active_products': active_products})

def category(request):
    return render(request, 'category.html')


class ProductList(generic.ListView):
    model = Products
    template_name = 'product.html'

def product(request, id):
    # product = Products.objects.get(id = ProductID)
    products = get_object_or_404(Products, id = ProductID)
    return render(request, 'product.html', {'products': products})

def combproduct(request):
    return render(request, 'combproduct.html')
