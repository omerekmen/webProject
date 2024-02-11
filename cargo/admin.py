from django.contrib import admin
from .models import *

@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = ('Order', 'CargoProvider', 'DeliveryStatus', 'TrackingNumber', 'MOKNumber', 'CargoTakenDate', 'CargoArrivalDate', 'EstimatedDeliveryDate') 
    list_editable = ('DeliveryStatus',)
    list_per_page = 25

    search_fields = [ 
        'OrderID__OrderID', 
        'TrackingNumber', 
        'MOKNumber',
        'DeliveryStatus',
        'CargoProvider',
    ]

    list_filter = [
        'OrderID__OrderID', 
        'TrackingNumber', 
        'MOKNumber',
        'DeliveryStatus',
        'CargoProvider',
    ]

@admin.register(CargoProvider)
class CargoProviderAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'ContactEmail', 'TelephoneNumber' ,'WebsiteURL')


