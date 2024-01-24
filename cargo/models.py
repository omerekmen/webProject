from django.db import models
from django.utils.translation import gettext_lazy as _
from orders.models import Orders

class CargoProvider(models.Model):
    CargoProviderID = models.AutoField(primary_key=True, verbose_name=_('Cargo Provider ID'))
    Name = models.CharField(_('Provider Name'), max_length=100)
    Description = models.TextField(_('Description'), blank=True, null=True)
    ContactEmail = models.EmailField(_('Contact Email'), blank=True, null=True)
    TelephoneNumber = models.CharField(_('Telephone Number'), max_length=20, blank=True, null=True)
    WebsiteURL = models.URLField(_('Website URL'), blank=True, null=True)

    class Meta:
        verbose_name = _("Kargo Sağlayıcıları")
        verbose_name_plural = _("Kargo Sağlayıcıları")

    def __str__(self):
        return self.Name

class Cargos(models.Model):
    OrderID = models.ForeignKey(Orders, verbose_name=_("Sipariş ID"), on_delete=models.CASCADE)
    CargoProvider = models.ForeignKey(CargoProvider, verbose_name=_('Kargo Sağlayıcı'), on_delete=models.SET_NULL, null=True, blank=True)
    TrackingNumber = models.CharField(_('KTN Numarası'), max_length=100, null=True, blank=True)
    MOKNumber = models.CharField(_("MÖK Numarası"), max_length=50, null=True, blank=True)
    CargoTakenDate = models.DateField(_("Kargoya Verilme Tarihi"), auto_now=False, auto_now_add=False)
    EstimatedDeliveryDate = models.DateField(_('Tahmini Teslim Tarihi'), null=True, blank=True)
    CargoArrivalDate = models.DateField(_("Kargo Teslim Tarihi"), auto_now=False, auto_now_add=False, null=True, blank=True)
    DeliveryStatus = models.CharField(_('Teslimat Durumu'), max_length=100, choices=[('Teslim Edildi', 'Teslim Edildi'), ('Dağıtıma Çıktı', 'Dağıtıma Çıktı'), ('Teslim Edilemedi', 'Teslim Edilemedi'), ('Kargo Aktarım Sürecinde','Kargo Aktarım Sürecinde')], default="Kargo Aktarım Sürecinde")

    class Meta:
        verbose_name = _("Sipariş Kargoları")
        verbose_name_plural = _("Sipariş Kargoları")
    
    def __str__(self):
        return str(self.OrderID_id) if self.OrderID else 'Cargos object'

