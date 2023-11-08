from django.urls import path
from store.views import *

urlpatterns = [
    path('', index, name='index'),
    path('kategori/', category, name='category' ),

    path('urun/', product, name='product'),
    path('urun/<ProductID>/', product, name='product' ),

    path('kombin/', combprod, name='combprod' ),
    path('kombin/<ProductID>/', combproduct, name='combproduct' ),

    path('sayfalar/<page_url>/', pages, name='pages' ),
    ]