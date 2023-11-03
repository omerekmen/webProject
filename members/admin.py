from django.contrib import admin
from .models import * 

class MemberAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/product_change_list.html'
    list_display = [
        'username',
        'first_name',
        'last_name',
        'birth_date',
        'user_type',
        'user_gender',
        'phone_number',
        'email',
    ]

    fieldsets = (
        ('User Info', {
            'fields': ('first_name', 'last_name', 'user_type', 'user_gender', 'birth_date'),
        }),
        ('Login Details', {
            'fields': ('username', 'password', 'last_login'),
        }),
        ('Contact Details', {
            'fields': ('email', 'phone_number'),
        }),
    )


# Register your models here.
admin.site.register(Campus)
admin.site.register(Member, MemberAdmin)