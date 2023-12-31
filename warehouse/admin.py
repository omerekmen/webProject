from django.contrib import admin
from .models import *
from .suppliers import *
from nested_admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin



@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'tax_no', 'email', 'phone', 'fax']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name', 'address', 'tax_no', 'email', 'phone', 'fax']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'tax_no', 'email', 'phone', 'fax']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name', 'address', 'tax_no', 'email', 'phone', 'fax']

class WaybillProductInline(admin.TabularInline):
    model = WaybillProduct
    extra = 0

@admin.register(Waybill)
class WaybillAdmin(admin.ModelAdmin):
    inlines = [WaybillProductInline]
    list_display = ['shipment', 'waybill_no', 'waybill_date']
    list_display_links = ['shipment', 'waybill_no']
    list_filter = ['shipment', 'waybill_no']
    search_fields = ['shipment', 'waybill_no']

class WaybillInline(admin.StackedInline):
    model = Waybill
    extra = 0
    inlines = [WaybillProductInline]

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    inlines = [WaybillInline]
    list_display = ['name', 'vehicle_type', 'manufacturer', 'supplier', 'warehouse',]
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name', 'vehicle_type', 'manufacturer', 'supplier', 'warehouse',]



@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'fax']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name', 'address', 'phone', 'fax']


@admin.register(WarehouseStock)
class WarehouseStockAdmin(admin.ModelAdmin):
    list_display = ['warehouse', 'product', 'stock']
    list_display_links = ['warehouse', 'product']
    list_filter = ['warehouse', 'product']
    search_fields = ['warehouse', 'product']