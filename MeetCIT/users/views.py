import sys

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse

from users.forms import CustomUserCreationForm

# Create your views here.


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    # If the view is displayed by a browser, then it will be accessed by a GET method.
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})

    # If the form is submitted, then the view will be accessed by a POST method. In that case, create a new user.
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # if valid, save the user and log the user in; then redirect to dashboard
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
