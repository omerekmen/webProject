from django.contrib import admin
from .models import *


class SupportMessageInline(admin.TabularInline):  # You can use StackedInline if you prefer that layout
    model = SupportMessage
    extra = 1

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    inlines = [SupportMessageInline]

    list_display = ['ticket_id', 'member', 'title', 'category', 'status', 'created_at', 'updated_at']


admin.site.register(SupportMessage)