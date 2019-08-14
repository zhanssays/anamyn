from django.conf.urls import url, re_path
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import LoginView, signup, home, logout_view, account_activation_sent, activate

app_name = 'account'

urlpatterns = [
    path("", home, name='index'),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", logout_view,  name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path("signup", signup, name='signup'),
    path("account_activation_sent", account_activation_sent, name='account_activation_sent'),
    path('activate/(<slug:uidb64>/<slug:token>/', activate, name='activate'),

]