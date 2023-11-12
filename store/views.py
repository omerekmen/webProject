from django.contrib.auth.decorators import login_required
from webProject.context_processors import get_school
from django.views import generic
from django.shortcuts import render
from products.models import *
from schools.models import *
from products.views import *
from members.urls import *
from datetime import datetime, timedelta


@login_required
def index(request):
    return render(request, 'store/index.html')

@login_required
def category(request):
    return render(request, 'store/category.html')

@login_required
def product(request, ProductID):
    product = Products.objects.get(school=get_school(), ProductID=ProductID, product_type='Tekil')

    related_products = Products.objects.filter(ProductSubCategoryID=product.ProductSubCategoryID).exclude(ProductID=ProductID)[:4]

    pcontext = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'store/product.html', pcontext)

@login_required
def combproduct(request, ProductID):
    product = Products.objects.get(school=get_school(), ProductID=ProductID, product_type='Kombin')

    pcontext = {
        'product': product,
    }

    return render(request, 'store/combproduct.html', {'product': product})





@login_required
def cart(request):
    return render(request, 'store/cart.html')

@login_required
def checkout(request):
    return render(request, 'store/checkout.html')

@login_required
def order(request):
    return render(request, 'store/order.html')





@login_required
def pages(request, page_url):
    school_pages = SchoolPages.objects.get(school=get_school(), page_url=page_url) 

    page_context = {
        'school_pages': school_pages,
    }

    return render(request, 'store/pages.html', page_context)


@login_required
def search(request):
    query = request.GET.get('search')
    products = Products.objects.filter(school=get_school(), product_web_name__icontains=query)

    context = {
        'search_products': products,
        'query': query,
    }

    return render(request, 'store/search.html', context)
