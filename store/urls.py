from django.urls import path, include
from django.conf.urls import handler404, handler500
from store.views import *
from orders.views import *
from store.account import *

urlpatterns = [
    path('', index, name='index'),
    path("", include('schools.urls')),
    path("user/", include('members.urls')),

    path("account/", account, name='account'),
    path('account/address/update/', address_update, name='address_update'),
    path('account/details/update/', account_details_update, name='account_details_update'),
    path('account/password/update/', password_update, name='password_update'),

    path('kategori/', category, name='category' ),
    path('kategoriler/<ProductCategoryID>', category_m, name='category_m' ),
    path('kategori/<ProductSubCategoryID>', category_p, name='category_p' ),

    path('urun/', product, name='product'),
    path('urun/<ProductID>/', product, name='product' ),

    path('kombin/', combproduct, name='combproduct' ),
    path('kombin/<ProductID>/', combproduct, name='combproduct' ),

    path('cart/', cart, name='cart' ),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('delete-from-cart/', delete_from_cart, name='delete_from_cart'),
    path('checkout/', checkout, name='checkout' ),
    path('create-order/', create_order, name='create_order' ),
    path('get-payment-details/', get_payment_details, name='get_payment_details' ),
    path('order/', order, name='order' ),

    path('sayfalar/<page_url>/', pages, name='pages' ),
    path('search/', search, name='search'),

    path('get-districts/', get_districts, name='get_districts'),
    path('get-student-class/', get_student_class, name='get_student_class'),
    ]
