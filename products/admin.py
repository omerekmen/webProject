from django.contrib import admin
from .models import *


class ProductSizeStockInline(admin.TabularInline):
    model = SizeBasedStocks
    verbose_name = 'Beden & Stok'
    verbose_name_plural = 'Beden & Stok'
    extra = 1  # Number of empty forms to display

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    verbose_name = 'Ürün Görselleri'
    verbose_name_plural = 'Ürün Görselleri'
    extra = 1  # Number of empty forms to display

class ProductPricesInline(admin.TabularInline):
    model = ProductPrices
    verbose_name = 'Ürün Fiyat'
    verbose_name_plural = 'Ürün Fiyat'
    extra = 1  # Number of empty forms to display


class ProductsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/product_change_list.html' 
    list_display = ('product_name', 'product_state', 'product_type', 'product_genre', 'product_color',)  # Customize the fields you want to display
    list_editable = ('product_state',)
    inlines = [ProductSizeStockInline, ProductPricesInline, ProductImagesInline]

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

    list_filter = [
        'product_state',
        'product_type', 
        'ProductCategoryID',
        'product_genre',
        'product_class',
        'product_level', 
        'product_color', 
    ]


    def make_inactive(self, request, queryset):
        queryset.update(product_state='Pasif')

    def make_active(self, request, queryset):
        queryset.update(product_state='Aktif')

    # Define the descriptions for your custom actions
    make_inactive.short_description = "Ürünleri Pasif Olarak İşaretle"
    make_active.short_description = "Ürünleri Aktif Olarak İşaretle"

    actions = [make_inactive, make_active]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.has_perm('products.view_bk_products') and request.user.groups.filter(name='bkAdmin').exists():
            return queryset.filter(school_management__contains='bk')
        elif request.user.has_perm('products.view_girne_products') and request.user.groups.filter(name='girneAdmin').exists():
            return queryset.filter(school_management__contains='girne')
        return queryset


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductCategorySizes)
admin.site.register(SizeBasedStocks)
admin.site.register(ProductPrices)
admin.site.register(CombinationProduct)
admin.site.register(SetProduct)