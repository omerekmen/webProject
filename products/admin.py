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

class ProductDetailsInline(admin.TabularInline):
    model = ProductDetails
    verbose_name = 'Ürün Detaylar'
    verbose_name_plural = 'Ürün Detaylar'
    extra = 1  # Number of empty forms to display


class ProductsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/product_change_list.html' 
    list_display = ('product_name', 'product_image', 'product_state', 'ProductSubCategoryID', 'product_type', 'product_genre', 'product_color', 'total_sale_stock')  # Customize the fields you want to display
    list_editable = ('product_state',)
    inlines = [ProductSizeStockInline, ProductPricesInline, ProductImagesInline, ProductDetailsInline]

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
        'ProductSubCategoryID', 
        'product_genre',
        'product_class',
        'product_level', 
        'product_color', 
    ]

    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('ProductSubCategoryID', 'product_type', 'product_state', 'product_production_name', 'product_name', 'product_web_name', 'model_code', 'product_color', 'book_type', 'product_genre', 'product_class', 'product_level', 'product_measure_unit', 'season', 'product_change_limit'),
        }),
        ('Ek Detaylar', {
            'fields': ('school_management', 'product_production_date', 'product_created_at', 'product_last_update'),
        }),
    )
    readonly_fields = ('product_created_at', 'product_last_update')


    def total_sale_stock(self, obj):
        # Calculate the total sale_stock for the product
        total_stock = SizeBasedStocks.objects.filter(products=obj).aggregate(total_sale_stock=models.Sum('sale_stock'))['total_sale_stock']
        return total_stock or 0
    
    total_sale_stock.short_description = 'Toplam Satış Stoğu'



    def make_inactive(self, request, queryset):
        queryset.update(product_state='Pasif')

    def make_active(self, request, queryset):
        queryset.update(product_state='Aktif')

    # Define the descriptions for your custom actions
    make_inactive.short_description = "Ürünleri Pasif Olarak İşaretle"
    make_active.short_description = "Ürünleri Aktif Olarak İşaretle"

    actions = [make_active, make_inactive]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.has_perm('products.view_bk_products') and request.user.groups.filter(name='bkAdmin').exists():
            return queryset.filter(school_management__contains='bk')
        elif request.user.has_perm('products.view_girne_products') and request.user.groups.filter(name='girneAdmin').exists():
            return queryset.filter(school_management__contains='girne')
        return queryset
    

class ProductSubCategoryInline(admin.TabularInline):
    model = ProductSubCategory
    verbose_name = 'Alt Kategori'
    verbose_name_plural = 'Alt Kategoriler'
    extra = 1 

class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = [ProductSubCategoryInline]
    list_display = ('CategoryName', 'get_subcategories')

class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('SubCategoryName', 'get_category_name')



admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
admin.site.register(ProductCategorySizes)
admin.site.register(SizeBasedStocks)
admin.site.register(ProductPrices)
admin.site.register(CombinationProduct)
admin.site.register(SetProduct)