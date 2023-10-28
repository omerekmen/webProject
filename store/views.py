from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render
from products.models import *
from products.views import *
from members.urls import *
from datetime import datetime, timedelta


# Functions to Manage Products
products = Products.objects.all()
active_products = Products.objects.filter(product_state='Aktif')

# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html', {'active_products': active_products})

@login_required(login_url='signin')
def category(request):
    return render(request, 'category.html')


class ProductList(generic.ListView):
    model = Products
    template_name = 'product.html'

@login_required(login_url='signin')
def product(request, id):
    # product = Products.objects.get(id = ProductID)
    products = get_object_or_404(Products, id = ProductID)
    return render(request, 'product.html', {'products': products})

@login_required(login_url='signin')
def combproduct(request):
    return render(request, 'combproduct.html')
