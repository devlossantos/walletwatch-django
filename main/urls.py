from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("password_recovery/", views.password_recovery, name="password_recovery"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("wallets/", views.wallets, name="wallets"),
    path("settings/", views.settings, name="settings"),
]