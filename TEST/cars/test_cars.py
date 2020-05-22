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

from SRC.Cars import Cars

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

