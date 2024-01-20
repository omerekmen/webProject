from django.urls import path, include
from django.conf.urls import handler404, handler500
from .views import *

urlpatterns = [
    # ... other URL patterns ...
    path('get-page-content/', get_page_content, name='get_page_content'),
]
