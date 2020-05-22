from . import Flights
from . import Hotels
from . import User
from . import Cars

class Travels:

    def __init__(self, flight: Flights, hotel: Hotels, coche: Cars, orig, dateI, dateF):
        self.flights = flight
        self.hotels = hotel
        self.cars = coche
        self.orig = orig
        self.dateI = dateI
        self.dateF = dateF


    def calcularPrecio(self):
        if self.flights.destination == "":
            self.price = 0
        else:
            self.price = self.hotels.getPrecio() * self.hotels.getPersones() + self.cars.getPrecio() + self.flights.getPrecio() * self.flights.get_nPassengers()
        return self.price

    def manage(self):
        pass

