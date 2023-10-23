from django.shortcuts import render
from store.models import Products

# Create your views here.

def product_list(request):
    products = Products.objects.all()  # Query to get all products from the database
    return render(request, 'index.html', {'products': products})