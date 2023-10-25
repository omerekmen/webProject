from django.contrib import admin
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'product_image',
        'product_name', 
        'product_type', 
        'product_production_name', 
        'product_color',
        'product_state', 
        'product_genre', 
        'product_class', 
        'product_level', 
        'product_created_at',
    ]

    list_filter = [
        'product_state',
        'product_type', 
        'ProductCategoryID',
        'CategorySizeID',
        'product_genre',
        'product_class',
        'product_level', 
        'product_color', 
        'product_sizes', 
    ]
    
    def Ürün_Adı(self, obj):
        return obj.product_name
    Ürün_Adı.short_description = 'Ürün Adı'

    search_fields = [
        'product_name', 
        'product_type', 
        'product_production_name', 
        'product_color', 
        'product_state', 
        'product_genre', 
        'product_class', 
        'product_level', 
    ]
    
    list_editable = ('product_state',)

    def make_inactive(self, request, queryset):
        queryset.update(product_state='Pasif')

    def make_active(self, request, queryset):
        queryset.update(product_state='Aktif')

    # Define the descriptions for your custom actions
    make_inactive.short_description = "Ürünleri Pasif Olarak İşaretle"
    make_active.short_description = "Ürünleri Aktif Olarak İşaretle"

    actions = [make_inactive, make_active]

# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductCategorySizes)
admin.site.register(ProductSize)
admin.site.register(ProductStock)
admin.site.register(ProductPrice)
admin.site.register(CombinationProduct)
admin.site.register(SetProduct)