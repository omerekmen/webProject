from django.contrib import admin
from .models import *

class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    verbose_name = 'Sipariş Ürün'
    verbose_name_plural = 'Sipariş Ürünler'
    extra = 1 

class OrderAdressInline(admin.TabularInline):
    model = OrderAddress
    verbose_name = 'Sipariş Adres'
    verbose_name_plural = 'Sipariş Adres'
    extra = 1 

class OrderPaymentInline(admin.TabularInline):
    model = OrderPayment
    verbose_name = 'Ödeme Detayları'
    verbose_name_plural = 'Ödeme Detayları'
    extra = 0

class OrderShippingInline(admin.TabularInline):
    model = OrderShipping
    verbose_name = 'Kargo Detayları'
    verbose_name_plural = 'Kargo Detayları'
    extra = 0

class OrdersAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/order_change_list.html' 
    list_display = ('OrderID', 'Member', 'memberName', 'memberCampus', 'OrderStatus', 'OrderDate')  # Customize the fields you want to display
    list_editable = ('OrderStatus',)
    inlines = [OrderProductsInline, OrderAdressInline, OrderPaymentInline, OrderShippingInline]

    search_fields = [
        'OrderID', 
        'Member', 
        'OrderStatus', 
        'OrderDate', 
    ]

    list_filter = [
        'OrderStatus',
        'OrderDate',
    ]
    readonly_fields = ('total_old_price', 'total_sale_price', 'total_discounted_sale_price', 'OrderDate', 'LastUpdatedAt', )

admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderProducts)