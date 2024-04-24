from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.static import static
from django.urls import path
from authentication.views import register_view, login_view
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Add other paths as needed
]