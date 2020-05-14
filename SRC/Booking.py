from . import User
from . import Hotels


class Booking():
    """
    Encapsula l'accés a la plataforma Booking.com per gestionar allotjaments

    El mètode confirm_reserve reb com a pàràmetres l'usuari que ha fet la pre-reserva i la llista d'hotels' que es volen reservar

    Les classes 'User' i 'Hotels' són classes pròpies de airhopping que heu de definir
    'Hotels' encapsula la API externa proporcionada per booking.com

    La classe 'User' conté informació de l'usuari que fa la reserva
    La classe 'Hotels' conté la llista d'hotels' pels quals es vol confirmar la reserva. De cada hotel té la següent informació:
    - Codi de l'hotel
    - Nom de l'hotel
    - Número d'hostes
    - Número d'habitacions
    - Durada en dies de la reserva
    """

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, hotels: Hotels) -> bool:
        return True
