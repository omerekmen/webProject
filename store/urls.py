from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('kategori/', category, name='category' ),

    path('urun/', product, name='product'),
    path('urun/<int:pk>/', product, name='product' ),

    path('kombin/', combproduct, name='combproduct' ),
    ]