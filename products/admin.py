from django.contrib import admin
from .models import *
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.forms.widgets import CheckboxSelectMultiple


class ProductSizeStockInline(admin.TabularInline):
    model = SizeBasedStocks
    verbose_name = 'Beden & Stok'
    verbose_name_plural = 'Beden & Stok'
    extra = 1 

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    verbose_name = 'Ürün Görselleri'
    verbose_name_plural = 'Ürün Görselleri'
    extra = 3

class ProductPricesInline(admin.TabularInline):
    model = ProductPrices
    verbose_name = 'Ürün Fiyat'
    verbose_name_plural = 'Ürün Fiyat'
    extra = 1

class ProductDetailsInline(admin.StackedInline):
    model = ProductDetails
    verbose_name = 'Ürün Detaylar'
    verbose_name_plural = 'Ürün Detaylar'
    extra = 1


# class MyCustomCheckboxSelectMultiple(CheckboxSelectMultiple):
#     # Override the JavaScript to select items by clicking
#     class Media:
#         js = ('my_custom_checkbox_select_multiple.js',)

# class CombinationProductInlineForm(forms.ModelForm):
#     class Meta:
#         model = CombinationProduct
#         widgets = {
#             'CombinProducts': MyCustomCheckboxSelectMultiple,
#         }
#         fields = '__all__'

class CombinationProductInline(admin.StackedInline):
    model = CombinationProduct
    verbose_name = 'Kombin Ürün Detaylar'
    verbose_name_plural = 'Kombin Ürün Detaylar'
    extra = 1
    # form = CombinationProductInlineForm


class ProductsResource(resources.ModelResource):
    class Meta:
        model = Products

class ProductsAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/product_change_list.html' 
    resource_class = ProductsResource
    inlines = [ProductSizeStockInline, ProductPricesInline, ProductImagesInline, ProductDetailsInline, CombinationProductInline]
    
    list_display = ('product_name', 'product_image', 'get_price', 'product_state', 'ProductSubCategoryID', 'product_type', 'product_genre', 'product_color', 'total_sale_stock')
    list_editable = ('product_state',)

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
            'fields': ('school', 'product_production_date', 'product_created_at', 'product_last_update'),
        }),
    )
    readonly_fields = ('product_created_at', 'product_last_update')

    def total_sale_stock(self, obj):
        total_stock = SizeBasedStocks.objects.filter(products=obj).aggregate(total_sale_stock=models.Sum('sale_stock'))['total_sale_stock']
        return total_stock or 0
    
    def get_price(self, obj):
        product_price = ProductPrices.objects.filter(products=obj).first()
        if product_price is not None:
            return product_price.SalePrice
        else:
            return 0
    
    total_sale_stock.short_description = 'Toplam Satış Stoğu'
    get_price.short_description = 'Satış Fiyatı'



    ##############################  CUSTOM ACTIONS  ##############################

    def make_inactive(self, request, queryset):
        queryset.update(product_state='Pasif')

    def make_active(self, request, queryset):
        queryset.update(product_state='Aktif')

    make_inactive.short_description = "Ürünleri Pasif Olarak İşaretle"
    make_active.short_description = "Ürünleri Aktif Olarak İşaretle"

    actions = [make_active, make_inactive]

    ##############################  CUSTOM ACTIONS  ##############################



    ############################  CUSTOM PERMISSIONS  ############################

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     if request.user.has_perm('products.view_bk_products') and request.user.groups.filter(name='bkAdmin').exists():
    #         return queryset.filter(school__contains='bahcesehir')
    #     elif request.user.has_perm('products.view_girne_products') and request.user.groups.filter(name='girneAdmin').exists():
    #         return queryset.filter(school__contains='girne')
    #     return queryset
    
    ############################  CUSTOM PERMISSIONS  ############################
    

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