from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
import datetime

# Define the StudentLevels model
class StudentLevels(models.Model):
    level_id = models.AutoField(primary_key=True)
    LevelName = models.CharField(max_length=100)  # Adjust max_length as needed
    CampusID = models.ForeignKey('Campus', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.LevelName}'
    

# Define the CampusAddress model
class CampusAddress(models.Model):
    CampusAddressID = models.AutoField(primary_key=True)
    FullAddress = models.CharField(max_length=255)
    District = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    PostalCode = models.IntegerField()
    AuthorizedFirstName = models.CharField(max_length=50)
    AuthorizedLastName = models.CharField(max_length=50)
    AuthorizedEmail = models.EmailField(max_length=100)
    AuthorizedPhone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.District}'

# Define the Campus model
class Campus(models.Model):
    campus_id = models.AutoField(primary_key=True)
    CampusAddressID = models.ForeignKey(CampusAddress, on_delete=models.CASCADE)
    FranchiseState = models.BooleanField()
    Phone = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)

    def __str__(self):
        return f'{self.CampusAddressID}'

# Define the Class model
class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    ClassName = models.CharField(max_length=255)
    ClassDescription = models.TextField()

    def __str__(self):
        return f'{self.ClassName}'

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser için is_staff=True olmalı!!!')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser için is_superuser=True olmalı!!!')
        
        return self.create_user(email, username, password, **other_fields)
    
    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError('Geçerli bir e-mail adresi girmeniz gerekiyor!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)

        user.set_password(password)
        user.save()

class Member(AbstractBaseUser, PermissionsMixin):
    member_id = models.AutoField(primary_key=True)

    email = models.EmailField(_('Email'), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    username = models.CharField(_('Username'), max_length=100, unique=True) # Öğrenci tarafında TC No alınacak
    first_name = models.CharField(_('Ad'), max_length=150, blank=True)
    last_name = models.CharField(_('Soyad'), max_length=150, blank=True)

    birth_date = models.DateField(_('Doğum Tarihi'), null=True, blank=True)

    USERTYPE_CHOICES = [('Öğrenci', 'Öğrenci'),
                        ('Mevcut Öğrenci', 'Mevcut Öğrenci'),
                        ('Kurumsal', 'Kurumsal'),
                        ('Kurum Admin', 'Kurum Admin'),
                        ('SuperUser', 'SuperUser'),
                        ]
    user_type = models.CharField(_('Kullanıcı Tipi'), max_length=100, choices=USERTYPE_CHOICES)
    user_gender = models.CharField("Cinsiyet", max_length=100, choices=[
                                                                        ('Erkek', 'Erkek'), 
                                                                        ('Kız', 'Kız')]
                                                                        )

    campus_id = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)
    level_id = models.ForeignKey(StudentLevels, on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

    is_active = models.BooleanField(_('Aktiflik Durumu'), default=True)
    is_staff = models.BooleanField(_('Aktiflik Durumu'), default=False)
    ip_address = models.CharField(_('IP Adres'), max_length=45)

    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.date.today().year + 2)]
    season = models.IntegerField("Sezon", choices=YEAR_CHOICES, default=datetime.date.today().year)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Üyeler'
        verbose_name_plural = 'Üyeler'

    def __str__(self):
        return f'{self.username}'