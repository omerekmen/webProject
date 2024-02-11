from django.db import models
from django.utils.translation import gettext_lazy as _
from school.models import PaymentGateways

# iyziSet = PaymentGateways.objects.get(payment_gateway='iyzico')
iyziSet = {
    'payment_api_key': "sandbox-",
    'secret_key': "",
    'base_url': ""
}