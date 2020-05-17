from . import User
from . import Cars


class Rentalcars():
    """
    Encapsula l'accés a la plataforma Rentalcars.com per gestionar cotxes

    El mètode confirm_reserve reb com a pàràmetres l'usuari que ha fet la pre-reserva i la llista de cotxes que es volen reservar

    Les classes 'User' i 'Cars' són classes pròpies de airhopping que heu de definir
    'Cars' encapsula la API externa proporcionada per Rentalcars.com

    La classe 'User' conté informació de l'usuari que fa la reserva
    La classe 'Cars' conté la llista de cotxes pels quals es vol confirmar la reserva. De cada cotxe té la següent informació:
    - Codi del cotxe
    - Marca del cotxe
    - Lloc de recollida
    - Durada en dies de la reserva
    """

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, cars: Cars) -> bool:
            if user.reserva == []:
                print("No existen reservas que confirmar\n")
            else:
                # Confirmar reserva de los coches
        return True
