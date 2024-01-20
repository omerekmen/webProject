from django.utils.translation import gettext_lazy as _
from django.db import models

from schools.models import *

class DiscountManagement(models.Model):
    pm_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

    double_discount = models.BooleanField(default=True, verbose_name="Özel İndirim & İndirim Kuponu", help_text="Bu ayar açık olduğunda Özel İndirim ve İndirim Kuponu aynı anda uygulanacaktır. Bu ayar kapalı ise sepette sadece önceğili 1 olan indirim uygulanacaktır.")
    sd_priority = models.CharField(max_length=100, choices=[('Yüksek', 'Yüksek'), ('Düşük', 'Düşük')], default="Yüksek", verbose_name="Özel İndirim Önceliği", help_text="1: Yüksek Öncelik | 2: Düşük Öncelik")
    dc_priority = models.CharField(max_length=100, choices=[('Yüksek', 'Yüksek'), ('Düşük', 'Düşük')], default="Düşük", verbose_name="İndirim Kuponu Önceliği", help_text="1: Yüksek Öncelik | 2: Düşük Öncelik")

    def save(self, *args, **kwargs):
        if self.sd_priority == self.dc_priority:
            self.sd_priority = 'Yüksek'
            self.dc_priority = 'Düşük'
        if self.double_discount:
            self.sd_priority = 'Yüksek'
            self.dc_priority = 'Düşük'

        super(DiscountManagement, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.school}'

    class Meta:
        verbose_name = "İndirim Önceliği Ayarı"
        verbose_name_plural = "İndirim Önceliği Ayarları"