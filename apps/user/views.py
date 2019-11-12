from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView


class ProfileView(TemplateView):
    template_name = 'user/profile.html'


class ProfileSettingsView(TemplateView):
    template_name = 'user/profile-settings.html'