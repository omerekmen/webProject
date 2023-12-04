from django.contrib import admin
from .models import * 

class MemberAddressInline(admin.TabularInline):
    model = MemberAddress
    verbose_name = 'Üye Adres'
    verbose_name_plural = 'Üye Adresler'
    extra = 1  # Number of empty forms to display

class MemberAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/product_change_list.html'
    inlines = [MemberAddressInline]
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

    # fieldsets = (
    #     ('User Info', {
    #         'fields': ('first_name', 'last_name', 'user_type', 'user_gender', 'birth_date'),
    #     }),
    #     ('Login Details', {
    #         'fields': ('username', 'password', 'last_login'),
    #     }),
    #     ('Contact Details', {
    #         'fields': ('email', 'phone_number'),
    #     }),
    # )


# Register your models here.
admin.site.register(Member, MemberAdmin)