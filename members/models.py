from django.db import models

# Create your models here.
"""
Members
-
memberID PK int
userType ENUM
identification VARCHAR(255) # TC No veya Pasaport No
password VARCHAR(255) # Şifrelenmiş password
firstName string
lastName string
phoneNumber int
email VARCHHAR(255)
birthDate Date 
gender ENUM 
weight Decimal(5,2)
height Decimal(4,2)
brandID int # Hiyerarşik olarak bağlı olunan şirket
vendorID int # Finansal olarak bağlı olunan şirket
campusID int # Bağlı olunan kampüs
levelName ENUM # Education Lvl (Primary School, High School)
classID int # Öğrencinin hangi sınıfa bağlı olduğu
registrationDate Date 
lastUpdated Ttimestamp
isActive Boolean
ipAdress VARCHAR(45)
registrationState ENUM # New or returning student
additionalData JSON
Season Date # Season Info

MemberAdress
--------------
id PK int
memberID int FK >- Members.memberID
adressLine1 VARCHAR(256)
adressLine2 VARCHAR(256)
city VARCHAR
country VARCHAR
phoneNumber int

I want you to create these models with connections
"""

class Members(models.Model):
    memberID = models.AutoField(primary_key=True)
    userType = models.CharField(max_length=20)
    identification = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=255)
    birthDate = models.DateTimeField()
    gender = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    brandID = models.IntegerField()
    vendorID = models.IntegerField()
    campusID = models.IntegerField()
    levelName = models.CharField(max_length=20)
    classID = models.IntegerField()
    registrationDate = models.DateTimeField()
    lastUpdated = models.DateTimeField()
    isActive = models.BooleanField()
    ipAdress = models.CharField(max_length=45)
    registrationState = models.CharField(max_length=20)
    additionalData = models.JSONField()
    Season = models.DateTimeField()

    def __str__(self):
        return self.firstName + " " + self.lastName
    

class MemberAddress(models.Model):
    id = models.AutoField(primary_key=True)
    memberID = models.ForeignKey(Members, on_delete=models.CASCADE)
    adressLine1 = models.CharField(max_length=256)
    adressLine2 = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    phoneNumber = models.IntegerField()

    def __str__(self):
        return self.adressLine1 + " " + self.adressLine2
        