class Flights:
    """
    - Codi del vol
    - Destinació
    - Número de passatgers

   """
    def __init__(self):

        self.flight_code = ""
        self.destination = ""
        self.n_passengers = 0

    def set_nPassengers(self, num: int):
        self.n_passengers = num

    def get_nPassengers(self):
        return self.n_passengers



