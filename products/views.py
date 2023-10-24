from django.shortcuts import render
from .models import Products

# Create your views here.
products = Products.objects.all()  # Query to get all products from the database
