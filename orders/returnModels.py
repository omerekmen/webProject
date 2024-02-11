from django.utils.translation import gettext_lazy as _
from django.db import models
from products.models import *  
from members.models import Member
from store.models import *  
from .models import *
import random
from datetime import datetime


class ReturnRequests(models.Model):
    ReturnID = models.SlugField(primary_key=True, editable=False, unique=True, max_length=10, verbose_name='İade Talep No')
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Sipariş No')
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='TC No')
    
    RETURN_STATUS_CHOICES = [
        ('İade Talebi Alındı', 'İade Talebi Alındı'),
        ('Talep İnceleniyor', 'Talep İnceleniyor'),
        ('Talep Onaylandı', 'Talep Onaylandı'),
        ('İade Bekleniyor', 'İade Bekleniyor'),
        ('İade İnceleniyor', 'İade İnceleniyor'),
        ('İade Edildi', 'İade Edildi')
    ]
    ReturnStatus = models.CharField(_('İade Talep Durumu'), max_length=100, choices=RETURN_STATUS_CHOICES, default="İade Talebi Alındı")

    ReturnPaymentAmount = models.DecimalField(_('İade Edilecek Tutar'), max_digits=10, decimal_places=2, default=0)
    RETURN_PAYMENT_STATUS_CHOICES = [
        ('Bekliyor', 'Bekliyor'),
        ('Ödeme Yapıldı', 'Ödeme Yapıldı'),
        ('Ödeme Yapılmadı', 'Ödeme Yapılmadı')
    ]
    ReturnPaymentStatus = models.CharField(_('İade Ödeme Durumu'), max_length=100, choices=RETURN_PAYMENT_STATUS_CHOICES, default="Bekliyor")
    ReturnPaymentDate = models.DateTimeField(_('İade Ödeme Tarihi'), blank=True, null=True)

    RETURN_REASON_CHOICES = [
        ('Ürün Arızalı', 'Ürün Arızalı'),
        ('Ürün Hasarlı', 'Ürün Hasarlı'),
        ('Ürün Yanlış', 'Ürün Yanlış'),
        ('Ürün Eksik', 'Ürün Eksik'),
        ('Ürün Değişim', 'Ürün Değişim'),
        ('Ürün İade', 'Ürün İade')
    ]
    ReturnReason = models.CharField(_('İade Nedeni'), max_length=100, choices=RETURN_REASON_CHOICES, default="Ürün Arızalı")

    ReturnNote = models.TextField(_('İade Notu'), blank=True, null=True)

    ReturnRequestDate = models.DateTimeField(_('İade Talep Tarihi'), auto_now_add=True)
    ReturnApprovedDate = models.DateTimeField(_('İade Onay Tarihi'), blank=True, null=True)
    ReturnCompletedDate = models.DateTimeField(_('İade Tamamlanma Tarihi'), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.ReturnID:
            self.ReturnID = self.create_return_id()
        if self.ReturnStatus == 'Talep Onaylandı' and not self.ReturnApprovedDate:
            self.ReturnApprovedDate = datetime.now()
        return super().save(*args, **kwargs)
    
    def create_return_id(self):
        last_return_id_num = 1
        return_id = f'RTN-{self.OrderID.OrderID}-{last_return_id_num:03}'
        while ReturnRequests.objects.filter(ReturnID=return_id).exists():
            last_return_id_num += 1
            return_id = f'RTN-{self.OrderID.OrderID}-{last_return_id_num:03}'
        return return_id

    class Meta:
        verbose_name = _('İade Talebi')
        verbose_name_plural = _('İade Talepleri')
        ordering = ['-ReturnRequestDate']

    def __str__(self):
        return f'{self.ReturnID}'
    

class ReturnProducts(models.Model):
    ReturnID = models.ForeignKey(ReturnRequests, on_delete=models.CASCADE, verbose_name='İade Talep No')
    OrderProductID = models.ForeignKey(OrderProducts, on_delete=models.CASCADE, verbose_name='Sipariş Ürün No')
    
    ProductPrice = models.DecimalField(_('Ürün Fiyatı'), max_digits=10, decimal_places=2, default=0)
    PaidAmount = models.DecimalField(_('Ödenen Tutar'), max_digits=10, decimal_places=2, default=0)
    
    ReturnQuantity = models.IntegerField(_('Ürün Adedi'), default=1)

    def save(self, *args, **kwargs):
        self.ProductPrice = self.OrderProductID.prod_sale_price
        self.PaidAmount = self.OrderProductID.discounted_sale_price / self.OrderProductID.Quantity * self.ReturnQuantity
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('İade Ürün')
        verbose_name_plural = _('İade Ürünler')
        ordering = ['-ReturnID']

    def __str__(self):
        return f'{self.ReturnID} - {self.OrderProductID}'
    