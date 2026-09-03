from django.urls import path
from .views import LoginView, LogoutView, ProfileView, SettingsView, SignupView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('signup/', SignupView.as_view(), name='signup'),
]
