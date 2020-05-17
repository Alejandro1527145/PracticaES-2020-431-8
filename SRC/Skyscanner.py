from . import User
from . import Flights


class Skyscanner():
    """
    Encapsula l'accés a la plataforma Skyscanner.com per gestionar vols

    El mètode confirm_reserve reb com a pàràmetres l'usuari que ha fet la pre-reserva i la llista de vols que es volen reservar

    Les classes 'User' i 'Flights' són classes pròpies de airhopping que heu de definir
    'Flights' encapsula la API externa proporcionada per Skyscanner.com

    La classe 'User' conté informació de l'usuari que fa la reserva
    La classe 'Flights' conté la llista de vols pels quals es vol confirmar la reserva. De cada vol té la següent informació:
    - Codi del vol
    - Destinació
    - Número de passatgers
    """

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        if user.reserva == []:
            print("No existen reservas que confirmar\n")
        else:
            print("¿Quiere confirmar la reserva para el vuelo con código de vuelo :\n",flights.flight_code)
            print("Confirma: si/no\n"")
            confirma = input()
            if(confirma == 'si'):
                # COMPROBAR QUE FLIGHTS NO ESTÉ VACÍO
                user.reserva.flights.flight_code = flights.flight_code
                user.reserva.flights.n_passengers = flights.n_passengers
                user.reserva.flights.destination = flights.destination
                print"Confirmación de la reserva: OK"
            else:
                print("No se ha realizado la confirmación de la reserva")

        return True
