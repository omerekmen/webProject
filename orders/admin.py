from django.contrib import admin
from .models import *

class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    verbose_name = 'Sipariş Ürün'
    verbose_name_plural = 'Sipariş Ürünler'
    extra = 1  # Number of empty forms to display

class OrderAdressInline(admin.TabularInline):
    model = OrderAddress
    verbose_name = 'Sipariş Adres'
    verbose_name_plural = 'Sipariş Adres'
    extra = 1  # Number of empty forms to display

class OrdersAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/order_change_list.html' 
    list_display = ('OrderID', 'Member', 'memberName', 'memberCampus', 'OrderStatus', 'OrderDate')  # Customize the fields you want to display
    list_editable = ('OrderStatus',)
    inlines = [OrderProductsInline, OrderAdressInline]

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

    # fieldsets = (
    #     ('Genel Bilgiler', {
    #         'fields': ('Member', 'OrderStatus', 'OrderDate'),
    #     }),
    #     ('Ek Detaylar', {
    #         'fields': ('OrderDate', 'LastUpdatedAt'),
    #     }),
    # )
    readonly_fields = ('OrderDate', 'LastUpdatedAt')

admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderProducts)