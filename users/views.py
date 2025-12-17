from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User


# SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role  # assign role directly
        )

        messages.success(request, "Signup successful. Please login.")
        return redirect("login")

    return render(request, "signup.html")


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("login")

        if user.role != role:
            messages.error(request, "Role mismatch")
            return redirect("login")

        login(request, user)

        if role == "doctor":
            return redirect("doctor_dashboard")
        else:
            return redirect("patient_dashboard")

    return render(request, "login.html")
