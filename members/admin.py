from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Members)
admin.site.register(StudentLevels)
admin.site.register(CampusAddress)
admin.site.register(Campus)
admin.site.register(Class)