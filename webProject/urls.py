from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from schools.views import fetch_content_for_modal
from wagtail.admin import urls as wagtailadmin_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('store.urls')),
    path('cms/', include(wagtailadmin_urls), name='wagtailadmin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('schools/', include('schools.urls')),  # Include your app's URLs
    path('fetch-modal-content/', fetch_content_for_modal, name='fetch_modal_content')
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
