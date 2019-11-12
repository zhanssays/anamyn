from django.urls import path
from .views import ProfileView, ProfileSettingsView

app_name = 'user'

urlpatterns = [
    path("", ProfileView.as_view(), name='profile'),
    path("settings", ProfileSettingsView.as_view(), name='profile-settings'),
]
