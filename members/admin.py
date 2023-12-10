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
    search_fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type', 'is_active', 'campus_id__campus_name']
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'get_school',
        'get_campus',
        'user_type',
        'registration_date',
        'is_active',
    ]

    list_filter = [
        'user_type',
        'campus_id__campus_name',
        'registration_date',
        'is_active',
    ]

    ##############################  CUSTOM ACTIONS  ##############################

    def make_inactive(self, queryset):
        queryset.update(is_active=False)

    def make_active(self, queryset):
        queryset.update(is_active=True)

    make_inactive.short_description = "Üyeleri Pasif Olarak İşaretle"
    make_active.short_description = "Üyeleri Aktif Olarak İşaretle"

    actions = [make_active, make_inactive]

    ##############################  CUSTOM ACTIONS  ##############################



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