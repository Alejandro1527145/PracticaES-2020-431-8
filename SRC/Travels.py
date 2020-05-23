from . import Flights
from . import Hotels
from . import User
from . import Cars

class Travels:

    def __init__(self):
        self.user = User()
        self.flights = Flights()
        self.hotels = Hotels()
        self.cars = Cars()
        self.orig = ""
        self.dateI = ""
        self.dateF = ""

    def __init__(self, user: User, flight: Flights, hotel: Hotels, coche: Cars, orig, dateI, dateF):
        self.user = user
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

    def confirmarReserva(self):
        print("Desea realizar la confirmación de la reserva con datos: \n")
        print("Usuario: ", self.user.name)
        print("Vuelos: ", self.flights.destination)
        if self.hotels.nombre != "":
            print("Hotel: ", self.hotels.nombre)
        if self.cars.marca != "":
        print("Código del coche: ", self.cars.codi)
        print("Marca del coche: ", self.cars.marca)

        print("S/N:")
        res = input()
        if res == "Si" or "S" or "Sí" or "s" or "si" or "sí":
            self.user.Travels = self
            print("Reserva confirmada")

        else:
            if res == "No" or "N" or "n" or "no":
                print("Reserva anulada")


