from . import Travels
from . import PaymentData
class User:

    def __init__(self):
        self.name = ""
        self.DNI = ""
        Travels.reserva = []
        PaymentData.tarjeta

    def __init__(self, name, DNI, telf, email, payment_data: PaymentData):
        self.name = name
        self.DNI = DNI
        self.telf = telf
        self.email = email
        self.payment_data = payment_data

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name