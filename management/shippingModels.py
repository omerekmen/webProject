from django.utils.translation import gettext_lazy as _
from django.db import models
from schools.models import Schools

class ShippingCost(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, verbose_name=_('Okul'))

    free_shipping_limit = models.DecimalField(_('Ücretsiz Kargo Limiti'), max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_cost_type = models.CharField(_('Kargo Ücreti Tipi'), max_length=100, choices=[('Kargo Ücreti Yok', 'Kargo Ücreti Yok'), ('Sabit Kargo Ücreti', 'Sabit Kargo Ücreti'), ('Ürün Bazlı Ücretlendirme', 'Ürün Bazlı Ücretlendirme')], default="Sabit Kargo Ücreti")
    shipping_cost = models.DecimalField(_('Kargo Ücreti'), max_digits=10, decimal_places=2, null=True, blank=True)

    return_shipping_cost_type = models.CharField(_('İade Kargo Ücreti Tipi'), max_length=100, choices=[('İade Kargo Ücreti Yok', 'İade Kargo Ücreti Yok'), ('Sabit İade Kargo Ücreti', 'Sabit İade Kargo Ücreti'), ('Ürün Bazlı İade Ücretlendirme', 'Ürün Bazlı İade Ücretlendirme')], default="Sabit İade Kargo Ücreti")
    return_shipping_payment = models.CharField(_('İade Kargo Ödemesi'), max_length=100, choices=[('Peşin Ödeme', 'Peşin Ödeme'), ('İade Tutarından Düş', 'İade Tutarından Düş')], default="Peşin Ödeme")
    return_shipping_cost = models.DecimalField(_('İade Kargo Ücreti'), max_digits=10, decimal_places=2, null=True, blank=True)

    change_shipping_cost_type = models.CharField(_('Değişim Kargo Ücreti Tipi'), max_length=100, choices=[('Değişim Kargo Ücreti Yok', 'Değişim Kargo Ücreti Yok'), ('Sabit Değişim Kargo Ücreti', 'Sabit Değişim Kargo Ücreti'), ('Ürün Bazlı Değişim Ücretlendirme', 'Ürün Bazlı Değişim Ücretlendirme')], default="Sabit Değişim Kargo Ücreti")
    change_shipping_cost = models.DecimalField(_('Değişim Kargo Ücreti'), max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = _('Kargo Ayarları')
        verbose_name_plural = _('Kargo Ayarları')

    def __str__(self):
        return f'{self.school} - Kargo Ücretleri'