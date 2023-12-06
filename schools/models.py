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
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=255)
    school_phone = models.CharField(max_length=15)
    school_subdomain = models.CharField(max_length=15)

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
    capmus_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    campus_name = models.CharField(max_length=255)
    campus_phone = models.CharField(max_length=15)
    campus_email = models.EmailField(max_length=255)
    franchise_state = models.BooleanField()

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
    level_id = models.AutoField(primary_key=True)
    LevelName = models.CharField(max_length=255)
    LevelDescription = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.LevelName}'
    
    class Meta:
        verbose_name = _("Seviye")
        verbose_name_plural = _("Seviyeler")

# Define the Class model
class Class(models.Model):
    LevelName = models.ForeignKey(StudentLevels, on_delete=models.CASCADE)
    ClassName = models.CharField(max_length=255)
    ClassDescription = models.TextField(null=True, blank=True)

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
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    school_intro_image = models.ImageField(upload_to=upload_location_settings, null=True, blank=True)
    school_logo_header = models.ImageField(upload_to=upload_location_settings, null=True, blank=True)
    school_header_title = models.CharField(max_length=255)
    school_logo_footer = models.ImageField(upload_to=upload_location_settings, null=True, blank=True)
    school_footer_title = models.CharField(max_length=255)
    school_footer_adress = models.TextField(null=True, blank=True)

    school_shop_adress = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Okul Ayarları")
        verbose_name_plural = _("Okul Ayarları")

    def __str__(self):
        return f'{self.school_header_title}'

class SchoolSlider(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    slider_image = models.ImageField(upload_to=upload_location_settings, null=True, blank=True)
    slider_title = models.CharField(max_length=255, default='Default Title')
    slider_description = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Okul Sliderları")
        verbose_name_plural = _("Okul Sliderları")

    def __str__(self):
        return f'{self.slider_title}'

class SchoolPages(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    page_title = models.CharField(max_length=255)
    page_category = models.CharField(max_length=50, choices=[('pages', 'Sayfalar'), ('contracts', 'Sözleşmeler')])
    page_url = models.SlugField(max_length=255, unique=True)
    footer_visibility = models.BooleanField(default=True)
    page_content = RichTextField()

    class Meta:
        verbose_name = _("Okul Sayfaları")
        verbose_name_plural = _("Okul Sayfaları")

    def __str__(self):
        return f'{self.page_title}'


class SchoolPopup(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    popup_page = models.CharField(max_length=100, choices=[('intro', 'Giriş Popup'), ('index', 'Anasayfa Popup'), ('product', 'Ürün Detay Popup')], null=True, blank=True)
    popup_title = models.CharField(max_length=15, null=True, blank=True)
    popup_content = RichTextField(null=True, blank=True)
    popup_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Popup Ayarları")
        verbose_name_plural = _("Popup Ayarları")

    def __str__(self):
        return f'{self.popup_title}'