from . import Flights
from . import Hotels
from . import User
from . import Cars

class Travels:

    def __init__(self, price, pasaj, orig, dateI, dateF):
        self.pasaj = pasaj
        self.orig = orig
        self.flights = Flights()
        self.hotels = Hotels()
        self.cars = Cars()
        self.dateI = dateI
        self.dateF = dateF
        self.price = price


    def calcularPrecio(self):
        for hotel in self.hotels:
            self.price = self.price + hotels.price
        for flight in self.flights:
            self.price = self.price + self.flights.price
        for car in self.cars:
            self.price = self.price + car.price

    def manage(self):
        pass



