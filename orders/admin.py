from cargo.models import Cargos
from django.contrib import admin
from .models import *
from .returnModels import *

class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    verbose_name = 'Sipariş Ürün'
    verbose_name_plural = 'Sipariş Ürünler'
    extra = 1 

class OrderAdressInline(admin.TabularInline):
    model = OrderAddress
    verbose_name = 'Sipariş Adres'
    verbose_name_plural = 'Sipariş Adres'
    extra = 1 

class OrderPaymentInline(admin.StackedInline):
    model = OrderPayment
    verbose_name = 'Ödeme Detayları'
    verbose_name_plural = 'Ödeme Detayları'
    extra = 0
    can_delete = False

class OrderShippingInline(admin.StackedInline):
    model = Cargos
    extra = 0
    verbose_name = 'Kargo'
    verbose_name_plural = 'Kargo Detayları'
    readonly_fields = ['CargoProvider', 'DeliveryStatus' , 'TrackingNumber', 'MOKNumber', 'CargoTakenDate', 'EstimatedDeliveryDate', 'CargoArrivalDate']
    can_delete = False


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/order_change_list.html' 
    list_display = ('OrderID', 'get_payment_provider', 'get_payment_id', 'Member', 'memberName', 'memberCampus', 'MemberClass', 'total_discounted_sale_price', 'OrderStatus', 'OrderDate','OrderWarehouseStatus')  # Customize the fields you want to display
    list_editable = ('OrderStatus',)
    inlines = [OrderProductsInline, OrderAdressInline, OrderPaymentInline, OrderShippingInline]
    list_per_page = 25
    change_list_template = 'admin/order_change_list.html'

    search_fields = [
        'Member', 
        'OrderStatus', 
        'OrderDate',
        'MemberClass',
    ]

    list_filter = [
        'OrderStatus',
        'OrderDate',
        'OrderWarehouseStatus',
        'MemberClass',
    ]
    readonly_fields = ('total_old_price', 'total_sale_price', 'total_discounted_sale_price', 'OrderDate', 'LastUpdatedAt', )

    def get_payment_provider(self, obj):
        payment = obj.order_payment.first()
        return payment.PaymentProvider if payment else 'Not Available'
    get_payment_provider.short_description = 'Ödeme Sağlayıcısı'

    def get_payment_id(self, obj):
        """Retrieve PaymentStatus from the first related OrderPayment instance."""
        payment = obj.order_payment.first()
        return payment.PaymentId if payment else 'Not Available'
    get_payment_id.short_description = 'Ödeme ID'

    def make_inactive(self, request, queryset):
        queryset.update(OrderWarehouseStatus=False)

    def make_active(self, request, queryset):
        queryset.update(OrderWarehouseStatus=True)

    make_inactive.short_description = "Depo Sürecini İptal Et"
    make_active.short_description = "Siparişi Depoya Aktar"

    actions = [make_active, make_inactive]


@admin.register(ReturnRequests)
class ReturnRequestsAdmin(admin.ModelAdmin):
    list_display = ('ReturnID', 'OrderID', 'Member', 'ReturnStatus', 'ReturnReason', 'ReturnRequestDate', 'ReturnApprovedDate', 'ReturnCompletedDate')
    list_editable = ('ReturnStatus',)
    list_per_page = 25

    search_fields = [
        'ReturnID', 
        'OrderID', 
        'Member', 
        'ReturnStatus', 
        'ReturnReason', 
        'ReturnRequestDate', 
        'ReturnApprovedDate', 
        'ReturnCompletedDate', 
    ]

    list_filter = [
        'ReturnStatus',
        'ReturnReason',
        'ReturnRequestDate',
        'ReturnApprovedDate',
        'ReturnCompletedDate',
    ]
    readonly_fields = ('ReturnID', 'ReturnRequestDate', 'ReturnApprovedDate', 'ReturnCompletedDate', )


admin.site.register(OrderProducts)
admin.site.register(TempOrderDetails)