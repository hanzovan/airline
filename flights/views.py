from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):

    # Get the flight information from flight_id
    flight = Flight.objects.get(pk=flight_id)

    # Get passengers information
    passengers = flight.passengers.all()

    # Get passenger that is not yet this flight's passenger
    non_passengers = Passenger.objects.exclude(flights=flight).all()

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })


def book(request, flight_id):
    # If request method = POST
    if request.method == "POST":
        
        # Get flight information
        flight = Flight.objects.get(pk=flight_id)

        # Get the passenger id
        passenger_id = request.POST["passenger"]

        # Get the passenger information from database
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add the flight to passenger's flight
        passenger.flights.add(flight)

        # Redirect user to the flight page
        return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))