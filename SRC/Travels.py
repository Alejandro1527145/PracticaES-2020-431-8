from . import Flights
from . import Hotels
from . import User
from . import Cars

class Travels:

    def __init__(self, preciovuelo, preciohotel, preciocoche, price, pasaj, orig, dateI, dateF):
        self.pasaj = pasaj
        self.orig = orig
        self.flights = Flights("", "", 0, preciovuelo)
        self.hotels = Hotels("", 0, 0, 0, 0, preciohotel)
        self.cars = Cars(0, "", "", 0, preciocoche)
        self.dateI = dateI
        self.dateF = dateF
        self.price = price


    def calcularPrecio(self):
        for hotel in self.hotels:
            self.price += self.hotels.getPrecio()
        for flight in self.flights:
            self.price += self.flights.getPrecio()
        for car in self.cars:
            self.price += self.cars.getPrecio()

    def manage(self):
        pass



