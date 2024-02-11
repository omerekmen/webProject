from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from school.models import *
from store.models import * 
import datetime


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_id = models.CharField(_('TC Kimlik No'), max_length=100, unique=True)
    email = models.EmailField(_('E-Posta'), unique=True)
    phone_number = models.IntegerField(_('Telefon'), null=True, blank=True)
    username = models.CharField(_('TC No'), max_length=100, unique=True)
    first_name = models.CharField(_('Ad'), max_length=150, blank=True)
    last_name = models.CharField(_('Soyad'), max_length=150, blank=True)

    birth_date = models.DateField(_('Doğum Tarihi'), null=True, blank=True)

    USERTYPE_CHOICES = [('Öğrenci', 'Öğrenci'),
                        ('Mevcut Öğrenci', 'Mevcut Öğrenci'),
                        ('Kurumsal', 'Kurumsal'),
                        ('Kurum Admin', 'Kurum Admin'),
                        ('SuperUser', 'SuperUser'),
                        ]
    USER_GENDER_CHOICES = [('Erkek', 'Erkek'), 
                            ('Kız', 'Kız')]
    user_type = models.CharField(_('Kullanıcı Tipi'), max_length=100, choices=USERTYPE_CHOICES, default='Öğrenci')
    user_gender = models.CharField("Cinsiyet", max_length=100, choices=USER_GENDER_CHOICES)

    campus_id = models.ForeignKey(SchoolCampus, on_delete=models.CASCADE, null=True, blank=True)
    level_id = models.ForeignKey(StudentLevels, on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

    is_active = models.BooleanField(_('Aktiflik Durumu'), default=True)
    ip_address = models.CharField(_('IP Adres'), max_length=45)

    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.date.today().year + 2)]
    season = models.IntegerField("Sezon", choices=YEAR_CHOICES, default=datetime.date.today().year)

    registration_date = models.DateTimeField(_('Kayıt Tarihi'), auto_now_add=True, null=True, blank=True)

    def get_campus(self):
        return self.campus_id.campus_name if self.campus_id else 'No Campus'

    def get_school(self):
        return self.campus_id.school.school_name if self.campus_id and self.campus_id.school else 'No School'

    get_campus.short_description = 'Kampüs'
    get_school.short_description = 'Okul'


    class Meta:
        verbose_name = 'Üyeler'
        verbose_name_plural = 'Üyeler'

    def __str__(self):
        return f'{self.username}'
    

class MemberAddress(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    AddressType = models.CharField(max_length=100, choices=[('Delivery', 'Teslimat'), ('Invoice', 'Fatura')])
    
    recipient_name = models.CharField(max_length=255, verbose_name="Alıcı Adı")
    recipient_lastname = models.CharField(max_length=255, verbose_name="Alıcı Soyadı")

    Country = models.CharField(max_length=100, default="Türkiye", verbose_name="Ülke")
    City = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="İl")
    District = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="İlçe")
    FullAddress = models.TextField(verbose_name="Adres")
    PostalCode = models.PositiveIntegerField(null=True, blank=True, verbose_name="Posta Kodu")

    PhoneNumber = models.IntegerField(verbose_name="Telefon Numarası")
    EMail = models.EmailField(verbose_name="E-Posta Adresi")

    comp_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Firma Adı")
    tax_office = models.CharField(max_length=255, null=True, blank=True, verbose_name="Vergi Dairesi")
    tax_no = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Vergi Numarası")

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""{self.recipient_name} {self.recipient_lastname}
            {self.PhoneNumber} / {self.EMail}
            {self.FullAddress} , {self.District.name}/{self.City.name}"""