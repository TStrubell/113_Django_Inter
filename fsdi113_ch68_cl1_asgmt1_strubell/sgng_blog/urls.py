"""
URL configuration for sgng_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from accounts.views import (
    LoginView,
    LogoutView,
    SignupView,
    ProfileView
)
from django.contrib.auth import views as auth_views
from sgng_blog.views import home, error_403, error_404, error_500

urlpatterns = [
    path('', home, name='home'),

    # Authentication
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # Signup
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/signup/success/', ProfileView.as_view(), name='signup_success'),

    # Profile
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

    # Password Change
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'
    ), name='password_change'),

    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),

    # Password Reset
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt'
    ), name='password_reset'),

    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    # 403 Forbidden
    path('403/', lambda request: render(request, '403.html'), name='forbidden'),

    # Email verification page
    path('accounts/verify/', lambda request: render(request, 'accounts/email_verification.html'), name='email_verification'),

    # User Settings Page
    path('accounts/settings/', lambda request: render(request, 'accounts/settings.html'), name='settings'),

    path('admin/', admin.site.urls),
]

# Error handlers
handler403 = error_403
handler404 = error_404
handler500 = error_500
