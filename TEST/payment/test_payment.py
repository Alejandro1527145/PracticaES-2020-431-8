import unittest

# TO BE ABLE TO DEBUG THE TEST 2 WAYS:
# 1: Configure PYTHONPATH
# 2: Add path to src folder manually (copy at the header of each test)
    # TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    # PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR,os.pardir))
    # PROJECT_DIR = os.path.join(PROJECT_DIR, '..','src')
    # if not PROJECT_DIR is sys.path:
    #   sys.path.insert(0, PROJECT_DIR)

from SRC.PaymentData import PaymentData
from SRC.User import User
from SRC.Bank import Bank
from SRC.Flights import Flights
from SRC.Hotels import Hotels
from SRC.Travels import Travels
from SRC.Cars import Cars

class TestPayment(unittest.TestCase):

    def test_tipus(self):
        self.Payment = PaymentData("", 0, 0, 0)
        assert self.Payment.type == ""
        assert not self.Payment.type == "VISA"
        self.Payment.type = "VISA"
        assert self.Payment.type == "VISA"
        self.Payment.setType("MASTERCARD")
        assert not self.Payment.type == "MASTERCARD"
        self.Payment.setType("MasterCard")
        assert self.Payment.type == "MasterCard"
        self.Payment.setType(123)
        assert not self.Payment.type == 123
        self.Payment = PaymentData("", 0, 0, 0)
        assert not self.Payment.type == "VISA"

    def test_pagament(self):
        self.Payment = PaymentData("", 0, 0, 0)
        self.User = User("", "", 0, "", self.Payment)
        self.Bank = Bank()
        assert self.Bank.do_payment(self.User,self.Payment) == True

    def test_mensaje_error(self):
        self.bank = Bank()
        self.Payment = PaymentData("","","",0)
        self.Usuari = User("","","","","")

        self.vol1 = Flights(1999, "Madrid", 1, 10)
        self.hotel1 = Hotels("a", 2, 1, 1, 1999, 10)
        self.cotxe1 = Cars(1999, "Ford Fiesta", "aeroport", 2, 10)
        self.Travels = Travels(self.Usuari, self.vol1, self.hotel1, self.cotxe1, "Barcelona", "23-06-2020", "01-07-2020")
        self.Travels.calcularPrecio()
        assert self.Travels.price == 30

        self.Payment.preu = self.Travels.getPrecio()

        self.payment_data = PaymentData('Jon Coello', '12345678900', '1234', 10)

        if self.bank.do_payment(self, self.payment_data):
            return True
        else:
            print('Error: No se ha podido realizar el pago correctamente.')
            return False



