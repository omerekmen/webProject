from django.db import models

# Define the StudentLevels model
class StudentLevels(models.Model):
    LevelID = models.AutoField(primary_key=True)
    LevelName = models.CharField(max_length=100)  # Adjust max_length as needed
    CampusID = models.ForeignKey('Campus', on_delete=models.CASCADE)

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

# Define the Campus model
class Campus(models.Model):
    CampusID = models.AutoField(primary_key=True)
    CampusAddressID = models.ForeignKey(CampusAddress, on_delete=models.CASCADE)
    FranchiseState = models.BooleanField()
    Phone = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)

# Define the Class model
class Class(models.Model):
    ClassID = models.AutoField(primary_key=True)
    ClassName = models.CharField(max_length=255)
    ClassDescription = models.TextField()

# Define the Members model
class Members(models.Model):
    MemberID = models.AutoField(primary_key=True)
    UserType = models.CharField(max_length=100)
    Identification = models.CharField(max_length=255, unique=True)
    PhoneNumber = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    BirthDate = models.DateField()
    Email = models.EmailField(max_length=255, unique=True)
    PasswordHash = models.CharField(max_length=255)
    CampusID = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)
    Gender = models.CharField(max_length=100)
    LevelID = models.ForeignKey(StudentLevels, on_delete=models.CASCADE, null=True, blank=True)
    ClassID = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    RegistrationState = models.CharField(max_length=100)
    RegistrationDate = models.DateTimeField()
    LastLogin = models.DateField()
    LastUpdated = models.DateTimeField()
    IsActive = models.BooleanField()
    IPAddress = models.CharField(max_length=45)
    Season = models.DateField()

    USERNAME_FIELD = 'Identification'

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
