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
        self.Flights = Flights(0,"",0,0)
        if (self.Flights.destination != ""):
            print ("Error en la creación de los destinos\n")
            quit()
        print ("El destino es correcto // OK \n")
        if (self.Flights.flight_code != 0):
            print ("Error en la creación del código de vuelo\n")
            quit()
        print ("El código de vuelo es correcto // OK \n")
        if (self.Flights.n_passengers != 0):
            print ("Error en la creación del número de pasajeros\n")
            quit()
        print ("El número de pasajeros es correcto // OK \n")
        return 1

    def test_1(self):
        self.Flights = Flights(0,"",0,0)
        self.Flights.destination = "Paris"
        self.Flights.flight_code = 1234
        self.Flights.n_passengers = 54

        if (self.Flights.destination != "Paris"):
            print ("Error en la creación de los destinos\n")
            quit()
        print ("El destino es correcto // OK \n")
        if (self.Flights.flight_code != 1234):
            print ("Error en la creación del código de vuelo\n")
            quit()
        print ("El código de vuelo es correcto // OK \n")
        if (self.Flights.n_passengers != 54):
            print("Error en la creación del número de pasajeros\n")
            quit()
        print("El número de pasajeros es correcto // OK \n")
        return 1

    def test_passengers(self):
        self.Flights = Flights(0,"",0,0)
        assert self.Flights.n_passengers == 0
        assert self.Flights.get_nPassengers() == 0
        self.Flights.n_passengers = 1
        assert self.Flights.n_passengers == 1
        assert self.Flights.get_nPassengers() == 1
        self.Flights.set_nPassengers(15)
        assert self.Flights.n_passengers == 15
        assert self.Flights.get_nPassengers() == 15

    def test_moreDestination(self):
        self.Flights = Flights(0, "", 0, 0)
        assert self.Flights.destination == ""
        self.Flights = Flights(0, "Madrid", 0, 0)
        assert self.Flights.destination == "Madrid"
        self.Flights.afegirDestins("Almeria")
        assert self.Flights.llista_d == ["Madrid", "Almeria"]
        self.Flights.afegirDestins("Mallorca")
        assert self.Flights.llista_d == ["Madrid", "Almeria", "Mallorca"]

    def test_moreFlights(self):
        self.Flights = Flights(0, "", 0, 0)
        assert self.Flights.flight_code == 0
        self.Flights = Flights(123, "Madrid", 0, 0)
        assert self.Flights.flight_code == 123
        self.Flights.afegirVols(145)
        assert self.Flights.llista_f == [123, 145]
        self.Flights.afegirVols(888)
        assert self.Flights.llista_f == [123, 145, 888]




