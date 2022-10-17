from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from helpers import days_between
from datetime import datetime, timedelta, date

# Create your views here.
@login_required
def index(request):

    today = str(date.today())
    the_day = "2023-02-13"
    return render(request, "users/index.html", {
        "days": days_between(today, the_day)
    })


# Let user login
def login_view(request):

    # If user already login, redirect back to index page
    if request.user.is_authenticated:

        return HttpResponseRedirect(reverse("users:index"))

    else:        

        if request.method == "POST":

            # Get username and password from the form
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password)

            # If authenticating fail
            if not user:
                return render(request, "users/login.html", {
                    "message": "Invalid Credentials"
                })

            # If success
            else:
                login(request, user)
                return HttpResponseRedirect(reverse("users:index"))

        else:
            return render(request, "users/login.html")


# Allow user to log out
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out successfully"
    })