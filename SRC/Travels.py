from . import Flights
from . import Hotels
from . import Cars
from . import User

class Travels:

    def __init__(self, user: User, flight: Flights, hotel: Hotels, coche: Cars, orig, dateI, dateF):
        self.user = user
        self.flights = flight
        self.hotels = hotel
        self.cars = coche
        self.orig = orig
        self.dateI = dateI
        self.dateF = dateF

    def getPrecio(self):
        return self.price

    def calcularPrecio(self):
        if self.flights.destination == "":
            self.price = 0
        else:
            self.price = self.hotels.getPrecio() * self.hotels.getPersones() + self.cars.getPrecio() + self.flights.getPrecio() * self.flights.get_nPassengers()
        return self.price