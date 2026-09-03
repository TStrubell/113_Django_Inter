from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render

class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'

class LogoutView(DjangoLogoutView):
    next_page = '/accounts/logout/'
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

class SettingsView(TemplateView):
    template_name = "accounts/settings.html"

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
