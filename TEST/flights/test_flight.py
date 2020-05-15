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

from SRC.Flights import Flights

class TestFlights(unittest.TestCase):

    def test_vacio(self):
        self.Flights = Flights()
        if (self.Flights.destination != ""):
            print ("Error en la creación de los destinos\n")
            quit()
        print ("El destino es correcto // OK \n")
        if (self.Flights.flight_code != ""):
            print ("Error en la creación del código de vuelo\n")
            quit()
        print ("El código de vuelo es correcto // OK \n")
        if (self.Flights.n_passengers != 0):
            print ("Error en la creación del número de pasajeros\n")
            quit()
        print ("El número de pasajeros es correcto // OK \n")
        return 1

    def Test_1(self):
        self.Flights = Flights()
        self.Flights.destination = "Paris"
        self.Flights.flight_code = "random_code"
        self.Flights.n_passengers = 54

        if (self.Flights.destination != "Paris"):
            print ("Error en la creación de los destinos\n")
            quit()
        print ("El destino es correcto // OK \n")
        if (self.Flights.flight_code != "random_code"):
            print ("Error en la creación del código de vuelo\n")
            quit()
        print ("El código de vuelo es correcto // OK \n")
        if (self.Flights.n_passengers != 54):
            print("Error en la creación del número de pasajeros\n")
            quit()
        print("El número de pasajeros es correcto // OK \n")
        return 1

    def Test_passengers(self):
        self.Flights = Flights()
        assert self.Flights.n_passengers == 0
        assert self.Flights.get_nPassengers() == 0
        self.Flights.n_passengers == 1
        assert self.Flights.n_passengers == 1
        assert self.Flights.get_nPassengers() == 1
        self.Flights.set_nPassengers(15)
        assert self.Flights.n_passengers == 15
        assert self.Flights.get_nPassengers() == 15

