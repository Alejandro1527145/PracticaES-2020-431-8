import unittest
from unittest import mock
from SRC.Cars import Cars
from SRC.Flights import Flights
from SRC.Hotels import Hotels
from SRC.PaymentData import PaymentData
from SRC.Travels import Travels
from SRC.User import User

class TestPrecio(unittest.TestCase):

    def test_sin_destino(self):
        self.Vuelo = Flights(0, "", 0, 5)
        self.Hotel = Hotels("", 0, 0, 0, 0, 5)
        self.Car = Cars(0, "", "", 0, 5)
        self.Usuari = User("","","","","")
        self.Travels = Travels(self.Usuari, self.Vuelo, self.Hotel, self.Car, "", "", "")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 0

    def test_calc_precio(self):
        self.vol1 = Flights(1999, "Madrid", 1, 10)
        self.hotel1 = Hotels("a", 2, 1, 1, 1999, 10)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 10)
        self.Usuari = User("", "", "", "", "")
        self.Travels = Travels(self.Usuari ,self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 30
        self.vol1 = Flights(1999, "Madrid", 1, 0)
        self.hotel1 = Hotels("a", 2, 1, 1, 1999, 0)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 0)
        self.Travels = Travels(self.Usuari, self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 0
        self.hotel1 = Hotels("a", 2, 1, 1, 1999, 5)
        self.Travels = Travels(self.Usuari, self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 5
        self.hotel1 = Hotels("a", 2, 1, 1, 1999, 5)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 5)
        self.Travels = Travels(self.Usuari, self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 10
        self.vol1 = Flights(1999, "Madrid", 1, 10)
        self.hotel1 = Hotels("a", 2, 2, 1, 1999, 0)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 5)
        self.Travels = Travels(self.Usuari, self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 15

        #MAS DE 1 PERSONA
        self.vol1 = Flights(1999, "Madrid", 2, 10)
        self.hotel1 = Hotels("a", 2, 1, 1, 1999, 10)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 10)
        self.Travels = Travels(self.Usuari, self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 40
        self.vol1 = Flights(1999, "Madrid", 2, 10)
        self.hotel1 = Hotels("a", 2, 2, 1, 1999, 10)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 10)
        self.Travels = Travels(self.Usuari,self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 50







