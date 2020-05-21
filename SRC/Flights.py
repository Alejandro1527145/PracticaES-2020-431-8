class Flights:
    """
    - Codi del vol
    - Destinació
    - Número de passatgers

   """
    def __init__(self):

        self.flight_code = 0
        self.destination = []
        self.n_passengers = 0
        self.price = 0

    def __init__(self, flight_code, destination, n_passengers, price):

        self.flight_code = flight_code
        self.destination = destination
        self.n_passengers = n_passengers
        self.price = price
        self.llista_d = []
        self.llista_d.append(self.destination)
        self.llista_f = []
        self.llista_f.append(self.flight_code)

    def set_nPassengers(self, num: int):
        self.n_passengers = num

    def get_nPassengers(self):
        return self.n_passengers

    def getPrecio(self):
        return self.price

    def afegirDestins(self, desti):
        self.llista_d.append(desti)
        return self.llista_d

    def afegirVols(self, codivol):
        self.llista_f.append(codivol)
        return self.llista_f




