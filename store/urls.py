from django.urls import path, include
from store.views import *

urlpatterns = [
    path('', index, name='index'),
    path("user/", include('members.urls')),

    path('kategori/', category, name='category' ),

    path('urun/', product, name='product'),
    path('urun/<ProductID>/', product, name='product' ),

    path('kombin/', combprod, name='combprod' ),
    path('kombin/<ProductID>/', combproduct, name='combproduct' ),

    path('sayfalar/<page_url>/', pages, name='pages' ),
    ]