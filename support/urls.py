from django.urls import path
from .views import *

urlpatterns = [
    path('admin/support_response/<str:ticket_id>/', support_response_view, name='support_response'),
    path('admin/admin_message_response/<str:ticket_id>/', admin_message_response, name='admin_message_response'),
    path('create_support_ticket/', create_support_ticket, name='create_support_ticket'),
]