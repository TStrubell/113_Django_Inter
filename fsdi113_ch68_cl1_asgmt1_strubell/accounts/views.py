from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'

class LogoutView(DjangoLogoutView):
    template_name = 'accounts/logout.html'

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('signup_success')

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'
