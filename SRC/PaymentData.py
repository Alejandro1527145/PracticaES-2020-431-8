class PaymentData:

    def __init__(self):
        self.type = ""
        self.titular = ""
        self.n_tarjeta = 0
        self.codi = 0
        self.preu = 0

    def setType(self, tipo: str):
        if (tipo == "VISA" or tipo == "MasterCard"):
            self.type = tipo


