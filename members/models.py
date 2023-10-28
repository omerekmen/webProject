from django.db import models
import datetime

# Define the StudentLevels model
class StudentLevels(models.Model):
    LevelID = models.AutoField(primary_key=True)
    LevelName = models.CharField("Sınıf", max_length=100)  # Adjust max_length as needed
    CampusID = models.ForeignKey('Campus', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.LevelName}"

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
        return f"{self.District}"

# Define the Campus model
class Campus(models.Model):
    CampusID = models.AutoField("Kampüs ID", primary_key=True)
    CampusAddressID = models.ForeignKey(CampusAddress, on_delete=models.CASCADE)
    FranchiseState = models.BooleanField()
    Phone = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.CampusAddressID}"

# Define the Class model
class Class(models.Model):
    ClassID = models.AutoField(primary_key=True)
    ClassName = models.CharField(max_length=255)
    ClassDescription = models.TextField()

    def __str__(self):
        return f"{self.ClassName}"

# Define the Members model
class Members(models.Model):
    MemberID = models.AutoField(primary_key=True)

    USERTYPE_CHOICES = [('Öğrenci', 'Öğrenci'),
                        ('Mevcut Öğrenci', 'Mevcut Öğrenci'),
                        ('Kurumsal', 'Kurumsal'),
                        ]
    UserType = models.CharField("Kullanıcı Tipi", max_length=100, choices=USERTYPE_CHOICES)
    Identification = models.CharField("Kimlik Numarası", max_length=255, unique=True)
    PhoneNumber = models.CharField("Telefon Numarası", max_length=20)
    FirstName = models.CharField("Ad", max_length=255)
    LastName = models.CharField("Soyad", max_length=255)
    BirthDate = models.DateField("Doğum Tarihi")
    Email = models.EmailField("E-Mail", max_length=255, unique=True)
    PasswordHash = models.CharField("Şifre", max_length=255)
    CampusID = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)
    Gender = models.CharField("Cinsiyet",max_length=100, choices=[('Erkek', 'Erkek'), ('Kız', 'Kız')])
    LevelID = models.ForeignKey(StudentLevels, on_delete=models.CASCADE, null=True, blank=True)
    ClassID = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    RegistrationState = models.CharField("Kayıt Durumu", max_length=100, choices=[('Mevcut','Mevcut'), ('Yeni', 'Yeni'),], default='Yeni')
    RegistrationDate = models.DateTimeField("Kayıt Tarihi", null=True)
    LastLogin = models.DateField("Son Giriş", null=True)
    LastUpdated = models.DateTimeField("Son Güncelleme", null=True)
    IsActive = models.BooleanField("Aktiflik Durumu", default=True)
    IPAddress = models.CharField("IP Adres", max_length=45)

    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.date.today().year + 2)]
    Season = models.IntegerField("Sezon", choices=YEAR_CHOICES, default=datetime.date.today().year)

    USERNAME_FIELD = 'Identification'

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
