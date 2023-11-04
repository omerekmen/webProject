from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render
from products.models import *
from products.views import *
from members.urls import *
from datetime import datetime, timedelta

sm= 'bk'

active_products = Products.objects.filter(product_state='Aktif', school_management=sm)
active_comb_products = Products.objects.filter(product_state='Aktif', product_type='Kombin', school_management=sm)

categories = ProductCategory.objects.all()
subcategories = ProductSubCategory.objects.all()

context = {
        'active_products': active_products, 
        'active_comb_products': active_comb_products, 
        'categories': categories,
        'subcategories': subcategories,
        }

def index(request):
    return render(request, 'store/index.html', context)


def category(request):
    return render(request, 'store/category.html', context)

def product(request):
    return render(request, 'store/product.html', context)

def combproduct(request):
    return render(request, 'store/combproduct.html', context)

