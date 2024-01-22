from django.urls import path, include
from django.conf.urls import handler404, handler500
from orders.views import *
from store.views import *
from cart.views import *
from store.account import *
from support.views import *

urlpatterns = [
    path('', index, name='index'),
    path("", include('schools.urls')),
    path("user/", include('members.urls')),

    path("account/", account, name='account'),
    path('account/address/update/', address_update, name='address_update'),
    path('account/details/update/', account_details_update, name='account_details_update'),
    path('account/password/update/', password_update, name='password_update'),
    path('account/support-messages/<str:ticket_id>/', get_support_messages, name='get_support_messages'),

    path('kategori/', category, name='category' ),
    path('kategoriler/<ProductCategoryID>', category_m, name='category_m' ),
    path('kategori/<ProductSubCategoryID>', category_p, name='category_p' ),

    path('urun/', product, name='product'),
    path('urun/<ProductID>/', product, name='product' ),

    path('kombin/', combproduct, name='combproduct' ),
    path('kombin/<ProductID>/', combproduct, name='combproduct' ),

    path('cart/', cart, name='cart' ),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('add-combined-to-cart/', add_combined_to_cart, name='add_combined_to_cart'),
    path('apply-coupon/', apply_coupon, name='apply_coupon'),
    path('update-cart-quantity/', update_cart_quantity, name='update_cart_quantity'),
    path('delete-from-cart/', delete_from_cart, name='delete_from_cart'),
    path('checkout/', checkout, name='checkout' ),
    path('create-order/', create_order, name='create_order' ),
    path('get-payment-details/', get_payment_details, name='get_payment_details' ),
    path('return-from-iyzico/', return_from_iyzico, name='return_from_iyzico' ),
    path('order/<OrderID>', order, name='order' ),
    path('order-details/<OrderID>', order_details, name='order_details' ),
    path('get-order-details/', get_order_details, name='get_order_details' ),
    path('order-error/', order_error, name='order_error' ),
    path('cancel-order/<int:order_id>/', cancel_order, name='cancel_order'),

    path('sayfalar/<page_url>/', pages, name='pages' ),
    path('search/', search, name='search'),

    path('get-districts/', get_districts, name='get_districts'),
    path('get-student-class/', get_student_class, name='get_student_class'),
    
    ]
