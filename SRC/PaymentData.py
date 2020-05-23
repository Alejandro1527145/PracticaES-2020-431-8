

class PaymentData:

    def __init__(self):
        self.type = ""
        self.titular = ""
        self.n_tarjeta = 0
        self.codi = 0
        self.preu = 0

    def __init__(self, titular, n_tarjeta, codi, preu):
        self.type = ""
        self.titular = titular
        self.preu = preu
        self.n_tarjeta = n_tarjeta
        self.codi = codi

    def setType(self, tipo: str):
        if (tipo == "VISA" or tipo == "MasterCard"):
            self.type = tipo

    def getPrecio(self):
        return self.preu



