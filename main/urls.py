from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("password_recovery/", views.password_recovery, name="password_recovery"),
    path("add_expense/", views.add_expense, name="add_expense"),
    path("expenses/", views.expenses, name="expenses"),
]