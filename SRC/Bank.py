from . import User
from . import PaymentData


class Bank:
    """
    Encapsula l'accés a la plataforma bancària per realitzar pagaments

    El mètode do_payment reb com a pàràmetres l'usuari que fa el pagament i les dades del pagament

    Les classes 'User' i 'PaymentData' són classes pròpies de airhopping que heu de definir

    La classe 'User' conté informació de l'usuari que fa el pagament
    La classe 'PaymentData' 'PaymentData' conté les dades necessàries per poder efectuar el pagament:
    - Tipus de targeta : VISA o Mastercard
    - Nom del titular (el que apareix a la targeta)
    - Número de la targeta
    - Codi de seguretat
    - Import
    """
    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        return True