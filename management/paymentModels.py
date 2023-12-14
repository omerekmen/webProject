from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentGateways(models.Model):
    pg_id = models.BigAutoField(primary_key=True, unique=True)
    payment_gateway = models.CharField(_('Ödeme Sağlayıcısı'), max_length=255, choices=[('iyzico', 'IyziPay'), ('param', 'Param'), ('ipara', 'iPara')])
    payment_base_url = models.CharField(_('API Url'), max_length=1000)
    payment_api_key = models.CharField(_('API Key'), max_length=1000, null=True, blank=True)
    payment_secret = models.CharField(_('API Secret Key'), max_length=1000, null=True, blank=True)
    payment_username = models.CharField(_('API Client Username'), max_length=1000, null=True, blank=True)
    payment_password = models.CharField(_('API Client Password'), max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = _('Ödeme Sağlayıcı')
        verbose_name_plural = _('Ödeme Sağlayıcıları')

    def __str__(self):
        return f'{self.payment_gateway}'