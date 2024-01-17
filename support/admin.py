from django.utils.html import format_html
from django.contrib import admin
from .models import *


class SupportMessageInline(admin.TabularInline):  # You can use StackedInline if you prefer that layout
    model = SupportMessage
    extra = 1

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    inlines = [SupportMessageInline]
    list_display = ['ticket_id', 'member', 'title', 'category', 'subject', 'status', 'created_at', 'updated_at', 'response_actions']

    def response_actions(self, obj):
        return format_html('<a style="text-align: center; cursor: pointer; padding: 0.5rem; color: #fff; background-color: #007bff; border-radius: 0.5rem;" href="/admin/support_response/{}">Görüntüle</a>', obj.ticket_id)

    response_actions.short_description = 'Aksiyonlar'


admin.site.register(SupportMessage)