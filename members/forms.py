from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from .models import Member
from schools.models import *
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(label='TC Kimlik Numarası', 
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label=_("Şifre"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    _("Lütfen geçerli bir kullanıcı adı ve şifre giriniz. Unutmayın, her iki alan da büyük/küçük harfe duyarlı olabilir."),
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    class Meta:
        model = Member
        fields = ('username')


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-Mail', max_length=254, required=True, help_text='Bu alan zorunludur. Lütfen geçerli bir mail adresi giriniz.',
                             widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='Öğrenci TC Kimlik Numarası', max_length=11, required=True,
                                widget=forms.NumberInput(attrs={"class": "form-control", "type": "number"}))
    phone_number = forms.CharField(label='Telefon Numarası',  max_length=17, required=True,
                                      widget=forms.NumberInput(attrs={"class": "form-control", "type":"number", "placeholder": "5__ ___ __ __"}))
    first_name = forms.CharField(label='Ad', max_length=100, required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Soyad', max_length=100, required=True, 
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    birth_date = forms.DateField(label='Doğum Tarihi', required=True, 
                                 widget=forms.DateInput(attrs={"autofocus": True, "class": "form-control", 'type': 'date', 'placeholder': '2000-01-01'})
                                 )
    
    user_type = forms.ChoiceField(
        choices=[('Öğrenci', 'Öğrenci'), ('Mevcut Öğrenci', 'Mevcut Öğrenci')],
        label='Kullanıcı Tipi',
        widget=forms.Select(attrs={"class": "form-control"})
    )
    user_gender = forms.ChoiceField(
        choices=Member.USER_GENDER_CHOICES,
        label='Cinsiyet',
        widget=forms.Select(attrs={"class": "form-control"})
    )
    campus_id = forms.ModelChoiceField(
        queryset=SchoolCampus.objects.all(),
        label='Kurum',
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False
    )
    level_id = forms.ModelChoiceField(
        queryset=StudentLevels.objects.all(),
        label='Kademe',
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False
    )
    class_id = forms.ModelChoiceField(
        queryset=Class.objects.all(),  # Initially empty, will be populated based on level_id
        label='Sınıf',
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False
    )

    ip_address = forms.CharField(label='', widget=forms.HiddenInput(), required=False)
    
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={"autofocus": True, "class": "form-control"}))
    password2 = forms.CharField(label='Şifre Tekrar', widget=forms.PasswordInput(attrs={"autofocus": True, "class": "form-control"}))


    class Meta:
        model = Member
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', 'ip_address', 'user_gender', 'user_type', 'campus_id', 'level_id', 'class_id' )