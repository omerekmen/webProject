from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render
from products.models import *
from products.views import *
from members.urls import *
from datetime import datetime, timedelta

school= '1'

active_products = Products.objects.filter(product_state='Aktif', school=school)
active_comb_products = Products.objects.filter(product_state='Aktif', product_type='Kombin', school=school)

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

def product(request, ProductID):
    product = Products.objects.get(ProductID=ProductID)

    pcontext = {
        'product': product,
    }

    return render(request, 'store/product.html', {'product': product})

def combproduct(request):
    return render(request, 'store/combproduct.html', context)

