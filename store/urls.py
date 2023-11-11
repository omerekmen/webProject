from django.urls import path, include
from django.conf.urls import handler404, handler500
from store.views import *

urlpatterns = [
    path('', index, name='index'),
    path("user/", include('members.urls')),

    path('kategori/', category, name='category' ),

    path('urun/', product, name='product'),
    path('urun/<ProductID>/', product, name='product' ),

    path('kombin/', combproduct, name='combproduct' ),
    path('kombin/<ProductID>/', combproduct, name='combproduct' ),

    path('sayfalar/<page_url>/', pages, name='pages' ),
    path('search/', search, name='search'),
    ]
