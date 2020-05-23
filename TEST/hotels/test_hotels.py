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


from SRC.Hotels import Hotels

class TestHotels(unittest.TestCase):

    def test_vacio(self):
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        if (self.Hotels.nombre != ""):
            print ("Error en la creación del nombre del hotel\n")
            quit()
        print ("El nombre de hotel es correcto // OK \n")
        if (self.Hotels.dias != 0):
            print ("Error en la creación de los dias de reserva")
            quit()
        print ("Los días de reservas son correctos // OK \n")
        if (self.Hotels.pers != 0):
            print ("Error en la creación del número de personas en la reserva\n")
            quit()
        print ("El número de personas de la reserva es correcto // OK \n")
        if (self.Hotels.precio != 0):
            print("Error en el precio de la reserva\n")
            quit()
        print ("El precio de la reserva es correcto // OK \n")
        if (self.Hotels.habitaciones != 0):
            print ("Error en la creación del número de habitaciones\n")
            quit()
        if (self.Hotels.id != ""):
            print("Error en la creación del id de la reserva\n")
            quit()
        print ("El número de id de la reserva es correto // OK \n")
        return 1

    def test_1(self):
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        self.Hotels.nombre = "Burj Al Arab"
        self.Hotels.pers = 4
        self.Hotels.habitaciones = 2
        self.Hotels.dias = 4
        self.Hotels.id = "d84-BAA"
        self.Hotels.precio = 5000

        if (self.Hotels.nombre != "Burj Al Arab"):
            print("Error en la creación del nombre del hotel\n")
            quit()
        print("El nombre de hotel es correcto // OK \n")
        if (self.Hotels.dias != 4):
            print("Error en la creación de los dias de reserva")
            quit()
        print("Los días de reservas son correctos // OK \n")
        if (self.Hotels.pers != 4):
            print("Error en la creación del número de personas en la reserva\n")
            quit()
        print("El número de personas de la reserva es correcto // OK \n")
        if (self.Hotels.precio != 5000):
            print("Error en el precio de la reserva\n")
            quit()
        print("El precio de la reserva es correcto // OK \n")
        if (self.Hotels.habitaciones != 2):
            print("Error en la creación del número de habitaciones\n")
            quit()
        if (self.Hotels.id != "d84-BAA"):
            print("Error en la creación del id de la reserva\n")
            quit()
        print("El número de id de la reserva es correto // OK \n")
        return 1

    def test_general(self):
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        assert self.Hotels.nombre == ""
        assert self.Hotels.getNombre() == ""
        self.Hotels.precio = 12332
        assert self.Hotels.precio == 12332
        assert self.Hotels.getPrecio() == 12332
        self.Hotels.id = "23423-OLOOK"
        assert self.Hotels.id == "23423-OLOOK"
        assert self.Hotels.getId() == "23423-OLOOK"
        self.Hotels.habitaciones = 10
        assert self.Hotels.habitaciones == 10
        assert self.Hotels.getHabitaciones() == 10
        self.Hotels.pers = 20
        assert self.Hotels.pers == 20
        assert self.Hotels.getPersones() == 20
        self.Hotels.dias = 10
        assert self.Hotels.dias == 10
        assert self.Hotels.dias == 10

    def test_nombre(self):
        # Inicialización desde constructor "Vacío"
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        assert self.Hotels.nombre == ""

        # Inicialización desde constructor "correcta"
        self.Hotels = Hotels("OverLook", 0, 0, 0, "", 0)
        assert self.Hotels.nombre == "OverLook"
        assert self.Hotels.getNombre() == "OverLook"

        # Inicialización desde constructor "mal"
        self.Hotels = Hotels(1, 0,0,0,"",0)
        assert self.Hotels.nombre == "Hotel"
        assert self.Hotels.getNombre() == "Hotel"

        # Inicialización desde igualación

        self.Hotels.nombre = "Wase"
        assert self.Hotels.nombre == "Wase"
        assert self.Hotels.getNombre() == "Wase"

    def test_id(self):
        # Inicialización desde constructor "Vacío"
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        assert self.Hotels.id == ""

        # Inicialización desde constructor "correcta"
        self.Hotels = Hotels("", 0, 0, 0, "12312", 0)
        assert self.Hotels.id == "12312"
        assert self.Hotels.getId() == "12312"

        # Inicialización desde constructor "mal"
        self.Hotels = Hotels("", 0,0,0,1,0)
        assert self.Hotels.id == "12-H"
        assert self.Hotels.getId() == "12-H"

        # Inicialización desde igualación
        self.Hotels.id = "13-H"
        assert self.Hotels.id == "13-H"
        assert self.Hotels.getId() == "13-H"

    def test_Habitaciones(self):
        # Inicialización desde constructor "Vacío"
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        assert self.Hotels.habitaciones == 0

        # Inicialización desde constructor "correcta"
        self.Hotels = Hotels("", 0, 0, 4, "", 0)
        assert self.Hotels.habitaciones == 4
        assert self.Hotels.getHabitaciones() == 4

        # Inicialización desde igualación
        self.Hotels.habitaciones = 4
        assert self.Hotels.habitaciones == 4
        assert self.Hotels.getHabitaciones() == 4

        # Modificación
        self.Hotels.habitaciones = 4
        self.Hotels.modificarHabitaciones(6,400)
        assert self.Hotels.habitaciones == 6
        assert self.Hotels.precio == 400

    def test_Pers(self):
        # Inicialización desde constructor "Vacío"
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        assert self.Hotels.pers == 0

        # Inicialización desde constructor "correcta"
        self.Hotels = Hotels("", 0, 4, 0, "", 0)
        assert self.Hotels.pers == 4
        assert self.Hotels.getPersones() == 4

        # Inicialización desde igualación
        self.Hotels.pers = 4
        assert self.Hotels.pers == 4
        assert self.Hotels.getPersones() == 4

        # Modificación
        self.Hotels.pers = 4
        self.Hotels.modificarPersonas(6, 400)
        assert self.Hotels.pers == 6
        assert self.Hotels.precio == 400

    def test_Dias(self):
        # Inicialización desde constructor "Vacío"
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        assert self.Hotels.dias == 0

        # Inicialización desde constructor "correcta"
        self.Hotels = Hotels("", 4, 0, 0, "", 0)
        assert self.Hotels.dias == 4
        assert self.Hotels.getDias() == 4

        # Inicialización desde igualación
        self.Hotels.dias = 4
        assert self.Hotels.dias == 4
        assert self.Hotels.getDias() == 4

        # Modificación
        self.Hotels.dias = 4
        self.Hotels.modificarDias(6, 400)
        assert self.Hotels.dias == 6
        assert self.Hotels.precio == 400

    def test_Precio(self):
        # Inicialización desde constructor "Vacío"
        self.Hotels = Hotels("", 0, 0, 0, "", 0)
        assert self.Hotels.precio == 0

        # Inicialización desde constructor "correcta"
        self.Hotels = Hotels("", 0, 0, 0, "", 400)
        assert self.Hotels.precio == 400
        assert self.Hotels.getPrecio() == 400

        # Inicialización desde igualación
        self.Hotels.precio = 400
        assert self.Hotels.precio == 400
        assert self.Hotels.getPrecio() == 400

        # Modificación
        self.Hotels.precio = 400
        self.Hotels.modificarPrecio(400)
        assert self.Hotels.precio == 400