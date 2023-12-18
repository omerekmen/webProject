from django.contrib import admin
from .mailModels import MailSettings
from .paymentModels import PaymentGateways
from .shippingModels import ShippingCost
from .discountModels import *

class DiscountManagementAdmin(admin.ModelAdmin):
    list_display = ('school', 'double_discount', 'sd_priority', 'dc_priority')
    # list_editable = ('double_discount', 'sd_priority', 'dc_priority')
    list_per_page = 25

class PaymentGatewaysAdmin(admin.ModelAdmin):
    # list_display = ('name', 'isActive', 'isDeleted', 'createdDate', 'updatedDate')
    # list_filter = ('name', 'isActive', 'isDeleted', 'createdDate', 'updatedDate')
    # list_display_links = ('name',)
    # search_fields = ('name', 'isActive', 'isDeleted', 'createdDate', 'updatedDate')
    list_per_page = 20

admin.site.register(PaymentGateways)
admin.site.register(MailSettings)
admin.site.register(ShippingCost)
admin.site.register(DiscountManagement, DiscountManagementAdmin)