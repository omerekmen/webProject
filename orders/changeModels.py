from django.utils.translation import gettext_lazy as _
from django.db import models
from products.models import *  
from members.models import Member
from store.models import *  
from .models import *
import random
from datetime import datetime


class ChangeRequests(models.Model):
    ChangeID = models.SlugField(primary_key=True, editable=False, unique=True, max_length=10, verbose_name='Değişim Talep No')
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Sipariş No')
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='TC No')
    
    ChangeStatus = models.CharField(_('Değişim Talep Durumu'), max_length=100, choices=[('Değişim Talebi Alındı', 'Değişim Talebi Alındı'), ('Talep İnceleniyor', 'Talep İnceleniyor'), ('Talep Onaylandı', 'Talep Onaylandı'), ('Değişim Bekleniyor', 'Değişim Bekleniyor'), ('Değişim İnceleniyor', 'Değişim İnceleniyor'), ('Değişim Edildi', 'Değişim Edildi')], default="Değişim Talebi Alındı")

    ChangePaymentAmount = models.DecimalField(_('Değişim Edilecek Tutar'), max_digits=10, decimal_places=2, default=0)
    ChangePaymentStatus = models.CharField(_('Değişim Ödeme Durumu'), max_length=100, choices=[('Bekliyor', 'Bekliyor'), ('Ödeme Yapıldı', 'Ödeme Yapıldı'), ('Ödeme Yapılmadı', 'Ödeme Yapılmadı')], default="Bekliyor")
    ChangePaymentDate = models.DateTimeField(_('Değişim Ödeme Tarihi'), blank=True, null=True)

    ChangeReason = models.CharField(_('Değişim Nedeni'), max_length=100, choices=[('Ürün Arızalı', 'Ürün Arızalı'), ('Ürün Hasarlı', 'Ürün Hasarlı'), ('Ürün Yanlış', 'Ürün Yanlış'), ('Ürün Eksik', 'Ürün Eksik'), ('Ürün Değişim', 'Ürün Değişim'), ('Ürün Değişim', 'Ürün Değişim')], default="Ürün Arızalı")

    ChangeNote = models.TextField(_('Değişim Notu'), blank=True, null=True)

    ChangeRequestDate = models.DateTimeField(_('Değişim Talep Tarihi'), auto_now_add=True)
    ChangeApprovedDate = models.DateTimeField(_('Değişim Onay Tarihi'), blank=True, null=True)
    ChangeCompletedDate = models.DateTimeField(_('Değişim Tamamlanma Tarihi'), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.ChangeID:
            self.ChangeID = self.create_Change_id()
        if self.ChangeStatus == 'Talep Onaylandı' and not self.ChangeApprovedDate:
            self.ChangeApprovedDate = datetime.now()
        return super().save(*args, **kwargs)
    
    def create_Change_id(self):
        last_change_id_num = 1
        Change_id = f'CHN-{self.OrderID.OrderID}-{last_change_id_num:03}'
        while ChangeRequests.objects.filter(ChangeID=Change_id).exists():
            last_Change_id_num += 1
            Change_id = f'CHN-{self.OrderID.OrderID}-{last_change_id_num:03}'
        return Change_id

    class Meta:
        verbose_name = _('Değişim Talebi')
        verbose_name_plural = _('Değişim Talepleri')
        ordering = ['-ChangeRequestDate']

    def __str__(self):
        return f'{self.ChangeID}'
    

class ChangeProducts(models.Model):
    ChangeID = models.ForeignKey(ChangeRequests, on_delete=models.CASCADE, verbose_name='Değişim Talep No')
    OrderProductID = models.ForeignKey(OrderProducts, on_delete=models.CASCADE, verbose_name='Sipariş Ürün No')
    
    ProductPrice = models.DecimalField(_('Ürün Fiyatı'), max_digits=10, decimal_places=2, default=0)
    PaidAmount = models.DecimalField(_('Ödenen Tutar'), max_digits=10, decimal_places=2, default=0)

    SelectedProduct = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Değişim Ürünü')
    SelectedProductSize = models.ForeignKey(ProductCategorySizes, on_delete=models.CASCADE, verbose_name='Değişim Ürünü Bedeni')
    SelectedProductPrice = models.DecimalField(_('Değişim Ürünü Fiyatı'), max_digits=10, decimal_places=2, default=0)
    
    ChangeQuantity = models.IntegerField(_('Ürün Adedi'), default=1)

    def save(self, *args, **kwargs):
        self.ProductPrice = self.OrderProductID.prod_sale_price
        self.PaidAmount = self.OrderProductID.discounted_sale_price / self.OrderProductID.Quantity * self.ChangeQuantity
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Değişim Ürün')
        verbose_name_plural = _('Değişim Ürünler')
        ordering = ['-ChangeID']

    def __str__(self):
        return f'{self.ChangeID} - {self.OrderProductID}'
    
