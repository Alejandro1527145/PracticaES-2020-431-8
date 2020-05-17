import unittest
from unittest import mock
import pytest
from SRC.Cars import Cars
from SRC.Flights import Flights
from SRC.Hotels import Hotels
from SRC.PaymentData import PaymentData
from SRC.Travels import Travels
from SRC.User import User

class TestPrecio(unittest.TestCase):

    def test_sin_des(self):

        Travels = Travels([0],[0],[0], 0, 2, 'Terrassa', '23-06-2020', '01-07-2020')
        Travels.calcularPrecio()
        assert Travels.price == 0

    def test_calc_precio(self):

        vol1 = Flights(1999, 'Madrid', 2, 10)
        vol2 = Flights(2000, 'Sevilla', 2, 20)

        hotel1 = Hotels('a', 2, 2, 1, 1999, 10)
        hotel2 = Hotels('b', 3, 2, 1, 2000, 20)

        cotxe1 = Cars(1999, 'Ford Fiesta', 'aeroport', 2, 10)
        cotxe2 = Cars(2000, 'Honda Cívic', 'aeroport', 2, 20)

        llistaV = [vol1, vol2]
        llistaH = [hotel1, hotel2]
        llistaC = [cotxe1, cotxe2]

        Travels = Travels(llistaV, llistaH, llistaC, 0, 2, 'Barcelona', '23-06-2020', '01-07-2020')
        Travels.calcularPrecio()
        preufinal = 30
        assert Travels.price == preufinal

