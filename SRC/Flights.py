class Flights:
    """
    - Codi del vol
    - Destinació
    - Número de passatgers

   """
    def __init__(self):

        self.flight_code = 0
        self.destination = ""
        self.n_passengers = 0
        self.price = 0

    def __init__(self, flight_code, destination, n_passengers, price):

        self.flight_code = flight_code
        self.destination = destination
        self.n_passengers = n_passengers
        self.price = price

    def set_nPassengers(self, num: int):
        self.n_passengers = num

    def get_nPassengers(self):
        return self.n_passengers

    def getPrecio(self):
        return self.price



