from django.contrib import admin
from .models import *


class SchoolSiteSettingsInline(admin.StackedInline):
    model = SchoolSiteSettings
    verbose_name = 'Site Ayarları'
    verbose_name_plural = 'Site Ayarları'
    extra = 1

class SchoolSliderInline(admin.StackedInline):
    model = SchoolSlider
    verbose_name = 'Slider Ayarları'
    verbose_name_plural = 'Slider Ayarları'
    extra = 0

class SchoolPagesInline(admin.StackedInline):
    model = SchoolPages
    verbose_name = 'Sayfalar'
    verbose_name_plural = 'Sayfalar'
    extra = 0
    inline_classes = ('collapse', )

class SchoolPopupInline(admin.StackedInline):
    model = SchoolPopup
    verbose_name = 'Popup Ayarları'
    verbose_name_plural = 'Popup Ayarları'
    extra = 1

class SchoolCampusInline(admin.StackedInline):
    model = SchoolCampus
    verbose_name = 'Kampüsler'
    verbose_name_plural = 'Kampüsler'
    extra = 0

class SchoolsAdmin(admin.ModelAdmin):
    inlines = [SchoolCampusInline, SchoolSiteSettingsInline, SchoolSliderInline, SchoolPagesInline, SchoolPopupInline]
    inline_classes = ('collapse', )
    list_display = ('school_name', 'school_logo', 'school_phone', 'school_subdomain', 'display_campuses')

    def display_campuses(self, obj):
        campuses = obj.schoolcampus_set.all()  # Get all campuses associated with the school
        return ', '.join([campus.campus_name for campus in campuses])
    display_campuses.short_description = 'Kampüsler'


admin.site.register(Schools, SchoolsAdmin)
admin.site.register(SchoolCampus)
admin.site.register(StudentLevels)
admin.site.register(Class)
