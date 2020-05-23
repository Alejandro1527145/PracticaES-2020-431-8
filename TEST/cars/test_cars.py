import os
import sys
import tempfile
import unittest

# TO BE ABLE TO DEBUG THE TEST 2 WAYS:
# 1: Configure PYTHONPATH
# 2: Add path to src folder manually (copy at the header of each test)
    # TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    # PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR,os.pardir))
    # PROJECT_DIR = os.path.join(PROJECT_DIR, '..','src')
    # if not PROJECT_DIR is sys.path:
    #   sys.path.insert(0, PROJECT_DIR)

from SRC.User import User
from SRC.Cars import Cars
from SRC.Hotels import Hotels
from SRC.Flights import Flights
from SRC.Travels import Travels
from SRC.PaymentData import PaymentData

class TestCars(unittest.TestCase):

    def test_inici(self):
        self.Car = Cars(0, "", "", 0, 0)
        assert self.Car.getPrecio() == 0
        self.Car = Cars(0, "", "", 0, 10)
        assert self.Car.getPrecio() == 10

    def test_addCars(self):
        self.Car = Cars(123, "BMW", "BCN", 5, 10)
        assert self.Car.getPrecio() == 10
        self.Car.afegirCotxe(321, "Audi", "BCN", 12, 5)
        assert self.Car.getPrecio() == 15

    def test_confirm_car(self):
        self.user1 = User("Juan", "48209943Q", 623841283, "juan@gmail.com", PaymentData("Juan", "763473998934", 312, 400))
        self.vol1 = Flights(1999, "Madrid", 1, 0)
        self.hotel1 = Hotels("a", 2, 1, 1, "1999", 0)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 7500)
        self.Travels = Travels(self.user1, self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")

        confirm = 0
        if self.cotxe1.getCodi() != 0 and self.cotxe1.getMarca() != 'None' and self.cotxe1.getRecollida() != 0 and self.cotxe1.getDies() != 0 and self.cotxe1.getPrecio() != 0:
            print('Confirmación Correcta')
            confirm = 1
        elif self.cotxe1.getCodi() == 0:
            print('No se ha podido confirmar la reserva del coche debido al código. ')
        elif self.cotxe1.getMarca() == 0:
            print('No se ha podido confirmar la reserva del coche debido a que no esta indicada la marca del coche.')
        elif self.cotxe1.getRecollida() == 0:
            print('No se ha podido confirmar la reserva del coche debido a que no estan indicadas las plazas del coche.')
        elif self.cotxe1.getDies() == 0:
            print('No se ha podido confirmar la reserva del coche debido a que no esta indicados los dias de alquiler del coche.')
        elif self.cotxe1.getPrecio() == 0:
            print('No se ha podido confirmar la reserva del coche debido a que no esta indicado el precio del coche.')
        if confirm !=0:
            return True
        else:
            return False

