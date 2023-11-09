from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render
from products.models import *
from schools.models import *
from products.views import *
from members.urls import *
from datetime import datetime, timedelta

# school= '1'

# active_products = Products.objects.filter(product_state='Aktif', school=school)
# active_comb_products = Products.objects.filter(product_state='Aktif', product_type='Kombin', school=school)

# categories = ProductCategory.objects.all()
# subcategories = ProductSubCategory.objects.all()

# context = {
#         'active_products': active_products, 
#         'active_comb_products': active_comb_products, 
#         'categories': categories,
#         'subcategories': subcategories,
#         }

def school(request, school=1):
    path = request.path # For sublinks
    subdomain = request.get_host().split('.')[0] ### FOR SUBDOMAINs

    # Define a mapping of subdomains to school IDs
    subdomain_to_school = {
        'bahcesehir': 1,
        'mektebim': 2,
        # Add more subdomains and their corresponding school IDs as needed
    }

    # Get the school ID based on the subdomain, default to 1 if not found
    sc = subdomain_to_school.get(subdomain, 1)

    parts = path.strip('/').split('/')
    sublink = parts[0]
    scl = subdomain_to_school.get(sublink, 1)

    return scl


def index(request):
    return render(request, 'store/index.html')


def category(request):
    return render(request, 'store/category.html')

def product(request, ProductID):
    product = Products.objects.get(school=school(request), ProductID=ProductID, product_type='Tekil')

    pcontext = {
        'product': product,
    }

    return render(request, 'store/product.html', {'product': product})

def combprod(request):

    return render(request, 'store/combproduct.html')

def combproduct(request, ProductID):
    product = Products.objects.get(school=school(request), ProductID=ProductID, product_type='Kombin')

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