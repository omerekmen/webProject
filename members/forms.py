from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Member


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )
    

    class Meta:
        model = User
        fields = ('username')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-Mail', max_length=254, required=True, help_text='Required. Inform a valid email address.',
                             widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='Öğrenci TC Kimlik Numarası', max_length=11, required=True,
                                widget=forms.NumberInput(attrs={"class": "form-control"}))
    phone_number = forms.IntegerField(label='Telefon Numarası', required=True,
                                      widget=forms.NumberInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='Ad', max_length=100, required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Soyad', max_length=100, required=True, 
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    birth_date = forms.DateField(label='Doğum Tarihi', 
                                 widget=forms.DateInput(attrs={"autofocus": True, "class": "form-control", 'placeholder': '2000-01-01'})
                                 )
    
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={"autofocus": True, "class": "form-control"}))
    password2 = forms.CharField(label='Şifre Tekrar', widget=forms.PasswordInput(attrs={"autofocus": True, "class": "form-control"}))

    class Meta:
        model = Member
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )