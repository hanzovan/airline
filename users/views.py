from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):

    # If user did not logged in, redirect to login page
    if not request.user.is_authenticated:
        
        return HttpResponseRedirect(reverse("users:login"))

    else:

        return render(request, "users/index.html")


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