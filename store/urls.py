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

    path('cart/', cart, name='cart' ),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout' ),
    path('order/', order, name='order' ),

    path('sayfalar/<page_url>/', pages, name='pages' ),
    path('search/', search, name='search'),
    ]
