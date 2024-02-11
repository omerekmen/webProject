from django.utils.translation import gettext_lazy as _
from django.db import models
from products.models import *  
from members.models import Member 
from store.models import *  
import random

class Orders(models.Model):
    OrderID = models.SlugField(primary_key=True, editable=False, unique=True, max_length=10, verbose_name='Sipariş No')
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='TC No')
    MemberClass = models.ForeignKey("school.Class", verbose_name=_("Üye Sınıfı"), on_delete=models.CASCADE, null=True, blank=True)

    ORDER_TYPE_CHOICES = [('Normal Sipariş', 'Normal Sipariş'), ('Bayi Siparişi', 'Bayi Siparişi')]
    OrderType = models.CharField(_('Sipariş Türü'), max_length=100, choices=ORDER_TYPE_CHOICES, default="Normal Sipariş")
    ORDER_STATUS_CHOICES = [('Sipariş Alındı', 'Sipariş Alındı'), ('Teslim Edildi', 'Teslim Edildi'), ('İptal Edildi', 'İptal Edildi'), ('İade Edildi', 'İade Edildi'), ('Değişim', 'Değişim')]
    OrderStatus = models.CharField(_('Sipariş Durumu'), max_length=100, choices=ORDER_STATUS_CHOICES, default="Sipariş Alındı")
    OrderWarehouseStatus = models.BooleanField(_("Depo Durumu"), default=False)
    OrderCargoFee = models.DecimalField(_('Kargo Ücreti'), max_digits=10, decimal_places=2, null=True, blank=True)

    SPECIAL_DISCOUNT_STATUS_CHOICES = [('Özel İndirim Yok', 'Özel İndirim Yok'), ('Öğrenci İndirimi', 'Öğrenci İndirimi'), ('Kampüs İndirimi', 'Kampüs İndirimi'), ('Kampanya İndirimi', 'Kampanya İndirimi')]
    SpecialDiscountStatus = models.CharField(_('Özel İndirim'), max_length=100, choices=SPECIAL_DISCOUNT_STATUS_CHOICES, default="Özel İndirim Yok")
    SpecialDiscount = models.DecimalField(_('Özel İndirim Tutarı'), max_digits=10, decimal_places=2, null=True, blank=True)
    CouponCode = models.CharField(_('Uygulanan Kupon Kodu'), max_length=100, null=True, blank=True)
    CouponDiscount = models.DecimalField(_('Kupon İndirimi'), max_digits=10, decimal_places=2, null=True, blank=True)
    
    def total_old_price(self):
        total = sum(item.prod_old_price * item.Quantity for item in self.user_order_items.all())
        return total

    def total_sale_price(self):
        total = sum(item.prod_sale_price * item.Quantity for item in self.user_order_items.all())
        return total

    def total_discounted_sale_price(self):
        total = sum(item.discounted_sale_price for item in self.user_order_items.all()) + self.OrderCargoFee - self.SpecialDiscount - self.CouponDiscount
        return total

    total_old_price.short_description = 'Toplam Eski Ürün Fiyatı'
    total_sale_price.short_description = 'TOPLAM ÜRÜN SATIŞ FİYATI'
    total_discounted_sale_price.short_description = 'TOPLAM TUTAR (Özel İndirimli)'
    

    def save(self, *args, **kwargs):
        if not self.OrderID:
            self.OrderID = self.generate_unique_order_id()

        if self.Member:
            self.MemberClass = self.Member.class_id

        super(Orders, self).save(*args, **kwargs)

    @staticmethod
    def generate_unique_order_id():
        range_start = 10**(4-1)
        range_end = (10**10)-1
        order_id = str(random.randint(range_start, range_end))

        while Orders.objects.filter(OrderID=order_id).exists():
            order_id = str(random.randint(range_start, range_end))
        return order_id
    
    def memberName(self):
        if self.Member:
            return f"{self.Member.first_name} {self.Member.last_name}"
        return None
    
    def memberCampus(self):
        if self.Member:
            return f"{self.Member.campus_id.campus_name}"
        return None
    
    
    memberName.short_description = 'Öğrenci Bilgileri'
    memberCampus.short_description = 'Öğrenci Şube'
    
    OrderNote = models.TextField(_('Sipariş Notları'), null=True, blank=True)


    OrderDate = models.DateTimeField(auto_now_add=True)
    LastUpdatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Siparişler")
        verbose_name_plural = _("Siparişler")
        ordering = ['-OrderDate']

    def __str__(self):
        return f"Order {self.OrderID}"

class OrderProducts(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Sipariş No', related_name='user_order_items')
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Ürün')

    is_combined_product = models.BooleanField(_('Kombin Ürün'), default=False)
    is_set_product = models.BooleanField(_('Set Ürün'), default=False)

    selected_size = models.ForeignKey(SizeBasedStocks, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Seçilen Beden')
    Quantity = models.IntegerField(_('Adet'), default=1)

    prod_old_price = models.DecimalField(_('Ürün Eski Fiyat'), max_digits=10, decimal_places=2, null=True, blank=True)
    prod_sale_price = models.DecimalField(_('Ürün Satış Fiyatı'), max_digits=10, decimal_places=2, null=True, blank=True)
    discounted_sale_price = models.DecimalField(_('Özel İndirimli Fiyat'), max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Sipariş Ürünleri")
        verbose_name_plural = _("Sipariş Ürünleri")

    def __str__(self):
        return f"{self.Product.product_name} - {self.Quantity} (pieces)"
    

class OrderCombinedProductChoice(models.Model):
    order_prod = models.ForeignKey(OrderProducts, on_delete=models.CASCADE, related_name='order_combined_product_choice')
    combination_product_category = models.ForeignKey(CombinationProduct, on_delete=models.CASCADE)
    selected_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size_stock = models.ForeignKey(SizeBasedStocks, on_delete=models.CASCADE, null=True, blank=True)


class OrderAddress(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_address')

    ADDRESS_TYPE_CHOICES = [('Teslimat', 'Teslimat'), ('Fatura', 'Fatura')]
    AddressType = models.CharField(max_length=100, choices=ADDRESS_TYPE_CHOICES)

    recipient_name = models.CharField(max_length=255)
    recipient_lastname = models.CharField(max_length=255)

    Country = models.CharField(max_length=100, default="Türkiye")
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    FullAddress = models.TextField()
    PostalCode = models.PositiveIntegerField(null=True, blank=True)

    PhoneNumber = models.IntegerField()
    EMail = models.EmailField()

    comp_name = models.CharField(max_length=255, null=True, blank=True)
    tax_office = models.CharField(max_length=255, null=True, blank=True)
    tax_no = models.PositiveBigIntegerField(null=True, blank=True)

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""{self.recipient_name} {self.recipient_lastname}
            {self.PhoneNumber} / {self.EMail}
            {self.FullAddress} , {self.District}/{self.City}"""


class OrderPayment(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_payment')

    PAYMENT_PROVIDER_CHOICES = [('iyzico', 'iyzico'), ('Diğer', 'Diğer')]
    PaymentProvider = models.CharField(max_length=100, choices=PAYMENT_PROVIDER_CHOICES, default="iyzico")
    PAYMENT_STATUS_CHOICES = [('Ödeme Alındı', 'Ödeme Alındı'), ('Ödeme Alınmadı', 'Ödeme Alınmadı')]
    PaymentStatus = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES, default="Ödeme Alındı")
    PaymentId = models.CharField(max_length=255)
    ConversationId = models.CharField(max_length=255)
    FRAUD_STATUS_CHOICES = [('-1', 'Yüksek Fraud Riski'), ('0', 'Fraud İhtimali'), ('1', 'Düşük Fraud Riski')]
    FraudStatus = models.CharField(max_length=100, choices=FRAUD_STATUS_CHOICES, default="1")
    Installment = models.PositiveIntegerField(null=True, blank=True)
    Currency = models.CharField(max_length=10, default="TRY")
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    PaidPrice = models.DecimalField(max_digits=10, decimal_places=2)
    iyziCommissionRateAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    iyziCommissionFee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    MerchantPayoutAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    CardType = models.CharField(max_length=100, null=True, blank=True)
    CardAssociation = models.CharField(max_length=100, null=True, blank=True)
    CardFamily = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.PaidPrice and self.iyziCommissionRateAmount and self.iyziCommissionFee:
            self.MerchantPayoutAmount = self.PaidPrice - self.iyziCommissionRateAmount - self.iyziCommissionFee
        else:
            self.MerchantPayoutAmount = None

        super(OrderPayment, self).save(*args, **kwargs)





class OrderShipping(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    


class TempOrderDetails(models.Model):
    tod_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    district_name = models.CharField(max_length=255)
    address = models.TextField()
    zip = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    invoice_city = models.CharField(max_length=100)
    invoice_city_name = models.CharField(max_length=100)
    invoice_district = models.CharField(max_length=100)
    invoice_district_name = models.CharField(max_length=255)
    invoice_address = models.TextField()
    invoice_phone = models.CharField(max_length=20)
    invoice_email = models.EmailField()
    comp_name = models.CharField(max_length=255)
    tax_office = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=100)

    order_notes = models.TextField(blank=True, null=True)
    different_address = models.BooleanField(default=False)
    save_address = models.BooleanField(default=False)

    conversation_id = models.CharField(max_length=100)
    token = models.CharField(max_length=255)

    def __str__(self):
        return f"OrderDetail for {self.member.username}"