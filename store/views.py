from django.contrib.auth.decorators import login_required
from webProject.context_processors import get_school
from django.views import generic
from django.shortcuts import render
from products.models import *
from schools.models import *
from products.views import *
from members.urls import *
from datetime import datetime, timedelta



def index(request):
    return render(request, 'store/index.html')


def category(request):
    return render(request, 'store/category.html')

def product(request, ProductID):
    product = Products.objects.get(school=get_school(), ProductID=ProductID, product_type='Tekil')

    pcontext = {
        'product': product,
    }

    return render(request, 'store/product.html', {'product': product})

def combprod(request):

    return render(request, 'store/combproduct.html')

def combproduct(request, ProductID):
    product = Products.objects.get(school=get_school(), ProductID=ProductID, product_type='Kombin')

    pcontext = {
        'product': product,
    }

    return render(request, 'store/combproduct.html', {'product': product})


def pages(request, page_url):
    school_pages = SchoolPages.objects.get(page_url=page_url) 

    page_context = {
        'school_pages': school_pages,
    }

    return render(request, 'store/pages.html', page_context)