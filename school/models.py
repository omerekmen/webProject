from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
# from django.urls import reverse

def upload_location(instance, filename):
    return f"school_files/{instance.Schools.school_name}/{filename}"


##########################################################################################
############################       SCHOOL and CAMPUS         #############################
##########################################################################################

class Schools(models.Model):
    school_name = models.CharField(max_length=255, verbose_name=_('Okul Adı'))
    school_phone = models.CharField(max_length=15, verbose_name=_('Telefon Numarası'))
    school_subdomain = models.CharField(max_length=15, verbose_name=_('Okul Domain'))

    def school_logo(self):
        # Get the first image for the product
        school_logo = SchoolSiteSettings.objects.filter(school=self).first()
        if school_logo:
            return mark_safe(f'<img src="{school_logo.school_logo_header.url}" height="50" />')
        return None
    
    school_logo.short_description = 'Logo'

    class Meta:
        verbose_name = _("Okullar")
        verbose_name_plural = _("Okullar")
        ordering = ['school_name']

    def __str__(self):
        return f'{self.school_name}'

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class SchoolCampus(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, verbose_name=_('Okul'))
    campus_name = models.CharField(max_length=255, verbose_name=_('Kampüs Adı'))
    campus_phone = models.CharField(max_length=15, verbose_name=_('Telefon Numarası'))
    campus_email = models.EmailField(max_length=255, verbose_name=_('E-mail Adresi'))
    franchise_state = models.BooleanField(verbose_name=_('Bayilik Durumu'))

    City = models.CharField(_('İl'), max_length=50, null=True, blank=True)
    District = models.CharField(_('İlçe'), max_length=50, null=True, blank=True)
    FullAddress = models.TextField(_('Tam Adres'), null=True, blank=True)
    PostalCode = models.IntegerField(_('Posta Kodu'), null=True, blank=True)
    AuthorizedFirstName = models.CharField(_('Yetkili Adı'), max_length=50, null=True, blank=True)
    AuthorizedLastName = models.CharField(_('Yetkili Soyadı'), max_length=50, null=True, blank=True)
    AuthorizedPhone = models.CharField(_('Yetkili Telefon'), max_length=15, null=True, blank=True)
    AuthorizedEmail = models.EmailField(_('Yetkili E-mail'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _("Kampüsler")
        verbose_name_plural = _("Kampüsler")

    def __str__(self):
        return f'{self.school.school_name} / {self.campus_name}'


# Define the StudentLevels model
class StudentLevels(models.Model):
    LevelName = models.CharField(max_length=255, verbose_name=_('Seviye Adı'))
    LevelDescription = models.TextField(null=True, blank=True, verbose_name=_('Seviye Açıklaması'))

    def __str__(self):
        return f'{self.LevelName}'
    
    class Meta:
        verbose_name = _("Seviye")
        verbose_name_plural = _("Seviyeler")

# Define the Class model
class Class(models.Model):
    LevelName = models.ForeignKey(StudentLevels, on_delete=models.CASCADE, verbose_name=_('Seviye'), related_name='level_class')
    ClassName = models.CharField(max_length=255, verbose_name=_('Sınıf Adı'))
    ClassDescription = models.TextField(null=True, blank=True, verbose_name=_('Sınıf Açıklaması'))

    def __str__(self):
        return f'{self.ClassName}'
    
    class Meta:
        verbose_name = _("Sınıf")
        verbose_name_plural = _("Sınıflar")
    

##########################################################################################
##############################       SCHOOL SETTINGS        ##############################
##########################################################################################


def upload_location_settings(instance, filename):
    return f"school_files/{instance.school.school_name}/{filename}"

class SchoolSiteSettings(models.Model):
    school = models.OneToOneField(Schools, on_delete=models.CASCADE, related_name='school_settings', verbose_name=_('Okul'))
    school_intro_image = models.ImageField(upload_to=upload_location_settings, null=True, blank=True, verbose_name=_('Giriş Resmi'))
    school_logo_header = models.ImageField(upload_to=upload_location_settings, null=True, blank=True, verbose_name=_('Header Logo'))
    school_header_title = models.CharField(max_length=255, verbose_name=_('Header Başlık'))
    school_logo_footer = models.ImageField(upload_to=upload_location_settings, null=True, blank=True, verbose_name=_('Footer Logo'))
    school_footer_title = models.CharField(max_length=255, verbose_name=_('Footer Başlık'))
    school_footer_adress = models.TextField(null=True, blank=True, verbose_name=_('Footer Adres'))

    school_shop_adress = models.TextField(null=True, blank=True, verbose_name=_('Mağaza Adresi'))

    class Meta:
        verbose_name = _("Okul Ayarları")
        verbose_name_plural = _("Okul Ayarları")

    def __str__(self):
        return f'{self.school_header_title}'

class SchoolSlider(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name='school_slider', verbose_name=_('Okul'))
    slider_image = models.ImageField(upload_to=upload_location_settings, null=True, blank=True, verbose_name=_('Slider Resmi'))
    slider_title = models.CharField(max_length=255, default='Default Title', verbose_name=_('Slider Başlık'))
    slider_description = RichTextField(null=True, blank=True, verbose_name=_('Slider Açıklaması'))

    class Meta:
        verbose_name = _("Okul Sliderları")
        verbose_name_plural = _("Okul Sliderları")

    def __str__(self):
        return f'{self.slider_title}'

class SchoolPages(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name='school_pages', verbose_name=_('Okul'))
    page_title = models.CharField(max_length=255)
    PAGE_CATEGORY_CHOICES =[('pages', 'Sayfalar'), ('contracts', 'Sözleşmeler')]
    page_category = models.CharField(max_length=50, choices=PAGE_CATEGORY_CHOICES, default='pages', verbose_name=_('Sayfa Kategorisi'))
    page_url = models.SlugField(max_length=255, unique=True, verbose_name=_('Sayfa URL'))
    footer_visibility = models.BooleanField(default=True, verbose_name=_('Footer Görünürlüğü'))
    page_content = RichTextField(verbose_name=_('Sayfa İçeriği'))

    class Meta:
        verbose_name = _("Okul Sayfaları")
        verbose_name_plural = _("Okul Sayfaları")

    def __str__(self):
        return f'{self.page_title}'


class SchoolPopup(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name='school_popup', verbose_name=_('Okul'))

    POPUP_PAGE_CHOICES = [('intro', 'Giriş Popup'), ('index', 'Anasayfa Popup'), ('product', 'Ürün Detay Popup')]
    popup_page = models.CharField(max_length=100, choices=POPUP_PAGE_CHOICES, null=True, blank=True, verbose_name=_('Popup Sayfası'))
    popup_image = models.ImageField(upload_to=upload_location_settings, null=True, blank=True, verbose_name=_('Popup Resmi'))
    popup_title = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Popup Başlık'))
    popup_content = RichTextField(null=True, blank=True, verbose_name=_('Popup İçeriği'))
    popup_status = models.BooleanField(default=True, verbose_name=_('Popup Durumu'))

    class Meta:
        verbose_name = _("Popup Ayarları")
        verbose_name_plural = _("Popup Ayarları")

    def __str__(self):
        return f'{self.popup_title}'



class ShippingCost(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name='school_shipping_cost', verbose_name=_('Okul'))

    SHIPPING_COST_CHOICES = [('Kargo Ücreti Yok', 'Kargo Ücreti Yok'), ('Sabit Kargo Ücreti', 'Sabit Kargo Ücreti'), ('Ürün Bazlı Ücretlendirme', 'Ürün Bazlı Ücretlendirme')]
    RETURN_SHIPPING_COST_CHOICES = [('Ücretsiz İade Kargo', 'Ücretsiz İade Kargo'), ('Sabit İade Kargo Ücreti', 'Sabit İade Kargo Ücreti'), ('Ürün Bazlı İade Ücretlendirme', 'Ürün Bazlı İade Ücretlendirme')]
    CHANGE_SHIPPING_COST_CHOICES = [('Değişim Kargo Ücreti Yok', 'Değişim Kargo Ücreti Yok'), ('Sabit Değişim Kargo Ücreti', 'Sabit Değişim Kargo Ücreti'), ('Ürün Bazlı Değişim Ücretlendirme', 'Ürün Bazlı Değişim Ücretlendirme')]

    free_shipping_limit = models.DecimalField(_('Ücretsiz Kargo Limiti'), max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_cost_type = models.CharField(_('Kargo Ücreti Tipi'), max_length=100, choices=SHIPPING_COST_CHOICES, default="Sabit Kargo Ücreti")
    shipping_cost = models.DecimalField(_('Kargo Ücreti'), max_digits=10, decimal_places=2, null=True, blank=True)

    return_shipping_cost_type = models.CharField(_('İade Kargo Ücreti Tipi'), max_length=100, choices=RETURN_SHIPPING_COST_CHOICES, default="Sabit İade Kargo Ücreti")
    return_shipping_payment = models.CharField(_('İade Kargo Ödemesi'), max_length=100, choices=[('Peşin Ödeme', 'Peşin Ödeme'), ('İade Tutarından Düş', 'İade Tutarından Düş')], default="Peşin Ödeme")
    return_shipping_cost = models.DecimalField(_('İade Kargo Ücreti'), max_digits=10, decimal_places=2, null=True, blank=True)

    change_shipping_cost_type = models.CharField(_('Değişim Kargo Ücreti Tipi'), max_length=100, choices=CHANGE_SHIPPING_COST_CHOICES, default="Sabit Değişim Kargo Ücreti")
    change_shipping_cost = models.DecimalField(_('Değişim Kargo Ücreti'), max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = _('Kargo Ayarları')
        verbose_name_plural = _('Kargo Ayarları')

    def __str__(self):
        return f'{self.school} - Kargo Ücretleri'


class PaymentGateways(models.Model):
    PAYMENT_GATEWAY_CHOICES = [('iyzico', 'IyziPay'), ('param', 'Param'), ('ipara', 'iPara')]
    payment_gateway = models.CharField(_('Ödeme Sağlayıcısı'), max_length=255, choices=PAYMENT_GATEWAY_CHOICES)
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


class DiscountManagement(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

    double_discount = models.BooleanField(default=True, verbose_name="Özel İndirim & İndirim Kuponu", help_text="Bu ayar açık olduğunda Özel İndirim ve İndirim Kuponu aynı anda uygulanacaktır. Bu ayar kapalı ise sepette sadece önceğili 1 olan indirim uygulanacaktır.")
    PRIORITY_CHOICES = [('Yüksek', 'Yüksek'), ('Düşük', 'Düşük')]
    sd_priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default="Yüksek", verbose_name="Özel İndirim Önceliği", help_text="1: Yüksek Öncelik | 2: Düşük Öncelik")
    dc_priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default="Düşük", verbose_name="İndirim Kuponu Önceliği", help_text="1: Yüksek Öncelik | 2: Düşük Öncelik")

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


class MailSettings(models.Model):
    mail_host = models.CharField(max_length=255, verbose_name='Mail Host')
    mail_port = models.IntegerField(verbose_name='Mail Port')
    mail_use_tls = models.BooleanField(default=True, verbose_name='Mail TLS')
    mail_username = models.CharField(max_length=255, verbose_name='Mail Username')
    mail_password = models.CharField(max_length=255, verbose_name='Mail Password')
    mail_from = models.CharField(max_length=255, verbose_name='Mail From')
    mail_def_from = models.CharField(max_length=255, verbose_name='Mail Default From')

    class Meta:
        verbose_name = 'Mail Ayarları'
        verbose_name_plural = 'Mail Ayarları'

    def __str__(self):
        return f'{self.mail_username}'