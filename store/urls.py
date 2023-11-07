from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('kategori/', category, name='category' ),

    path('urun/', product, name='product'),
    path('urun/<ProductID>/', product, name='product' ),

    path('kombin/', combproduct, name='combproduct' ),
    ]