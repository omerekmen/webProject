from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Members

class MemberRegisterForm(UserCreationForm):

    class Meta:
        model = Members
        fields = [
            'Identification', 
            'PhoneNumber',
            'FirstName',
            'LastName',
            'BirthDate',
            'Email',
            'CampusID',
            'Gender',
            'LevelID',
            'ClassID',
            'RegistrationState',
        ]

    