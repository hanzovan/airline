from django.shortcuts import render
from .models import Flight, Airport, Passenger


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
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers
    })