from . import Flights
from . import Hotels
from . import User

class Travels:

    def __init__(self, flights, hotels, cars, price, pasaj, orig, dateI, dateF):
        self.pasaj = pasaj
        self.orig = orig
        self.flights = flights
        self.hotels = hotels
        self.cars = cars
        self.dateI = dateI
        self.dateF = dateF
        self.price = price

    def calcularPrecio(self):
        for hotel in self.hotels:
            self.price = self.price + hotel.price
        for flight in self.flights:
            self.price = self.price + flight.price
        for car in self.cars:
            self.price = self.price + car.price

    def manage(self):
        pass



