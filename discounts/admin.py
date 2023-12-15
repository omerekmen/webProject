from django.contrib import admin
from .models import *

class SpecialDiscountAdmin(admin.ModelAdmin):
    list_display = ('discountName', 'discountStatus', 'discountAmountbyType', 'cargoDiscountCheck', 'products_list', 'discountStartDate', 'discountEndDate')
    list_filter = ('school', 'discountStatus', 'discountStartDate', 'discountEndDate')
    search_fields = ('discountName', 'school', 'discountStatus', 'discountStartDate', 'discountEndDate')
    list_per_page = 25

    def discountAmountbyType(self, obj):
        if obj.discountType == 'percentage':
            return f'{obj.discountAmount}%'
        else:
            return f'{obj.discountAmount}₺'
    discountAmountbyType.short_description = 'İndirim Miktarı'

    def cargoDiscountCheck(self, obj):
        if obj.cargoDiscount:
            return f'{obj.cargoDiscountAmount}%'
        else:
            return 'İndirim Yok'
    cargoDiscountCheck.short_description = 'Kargo İndirimi'

    def products_list(self, obj):
        products = obj.products.all()
        if products.count() > 3:
            product_names = '<br>'.join([product.product_web_name for product in products[:3]])
            return mark_safe(f'{product_names}<br>...')
        else:
            product_names = '<br>'.join([product.product_web_name for product in obj.products.all()])
            return mark_safe(product_names)

class DiscountCouponAdmin(admin.ModelAdmin):
    list_display = ('discountName', 'discountStatus', 'discountAmountbyType', 'cargoDiscountCheck', 'products_list', 'discountStartDate', 'discountEndDate')
    list_filter = ('school', 'discountStatus', 'discountStartDate', 'discountEndDate')
    search_fields = ('discountName', 'school', 'discountStatus', 'discountStartDate', 'discountEndDate')
    list_per_page = 25

    def discountAmountbyType(self, obj):
        if obj.discountType == 'percentage':
            return f'{obj.discountAmount}%'
        else:
            return f'{obj.discountAmount}₺'
    discountAmountbyType.short_description = 'İndirim Miktarı'

    def cargoDiscountCheck(self, obj):
        if obj.cargoDiscount:
            return f'{obj.cargoDiscountAmount}%'
        else:
            return 'İndirim Yok'
    cargoDiscountCheck.short_description = 'Kargo İndirimi'

    def products_list(self, obj):
        products = obj.products.all()
        if products.count() > 3:
            product_names = '<br>'.join([product.product_web_name for product in products[:3]])
            return mark_safe(f'{product_names}<br>...')
        else:
            product_names = '<br>'.join([product.product_web_name for product in obj.products.all()])
            return mark_safe(product_names)

admin.site.register(SpecialDiscount, SpecialDiscountAdmin)
admin.site.register(DiscountCoupon, DiscountCouponAdmin)
