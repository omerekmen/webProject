from django.urls import path
from .views import * 

urlpatterns = [
    path("iyzico_pay/", iyzico_pay, name='iyzico_pay'),
]