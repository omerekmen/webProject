from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductCategory)
admin.site.register(ProductCategorySizes)
admin.site.register(ProductStock)
admin.site.register(ProductPrice)
admin.site.register(CombinationProduct)
admin.site.register(SetProduct)