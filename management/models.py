from django.db import models
from .mailModels import MailSettings

mailSet = MailSettings.objects.first()