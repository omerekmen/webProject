from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import * 

urlpatterns = [
    path("register/", register_view, name='register'),
    path("login/", login_view, name='login'),
    path("logout/", custom_logout, name='logout'),
]
