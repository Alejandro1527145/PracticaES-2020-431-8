from . import Travels
from . import PaymentData
class User:

    def __init__(self):
        self.name = ""
        self.DNI = ""
        Travels.reserva = []
        PaymentData.tarjeta

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name;