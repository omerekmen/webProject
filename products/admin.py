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
    list_display = ('product_name', 'product_state', 'product_type', 'product_genre', 'SKU_code', 'product_color',)  # Customize the fields you want to display
    list_editable = ('product_state',)
    inlines = [ProductSizeStockInline, ProductPricesInline, ProductImagesInline]

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