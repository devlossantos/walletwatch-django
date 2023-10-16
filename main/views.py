from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == "POST":
        username = request.POST["form_username"]
        password = request.POST["form_password"]
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, ("Invalid username or password."))
            return redirect("home")
    else:
        return render(request, "home.html", {})

def signup(request):
    return render(request, "signup.html")

def signout(request):
    logout(request)
    return redirect("home")

def password_recovery(request):
    return render(request, "password_recovery.html")

def add_expense(request):
    return render(request, "add_expense.html")

def expenses(request):
    return render(request, "expenses.html")
