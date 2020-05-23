class Hotels:

    def __init__(self, nombre: str, dias: int, pers: int, habitaciones: int, id: str, precio: int):
        while type(id) != str:
           print("El ID de la reserva debe de ser una cadena de carácteres.\n")
           print("Vuelva a introducirlo de nuevo:\n")
           id = input()
        self.id = id
        while type(nombre) != str:
           print("El nombre del hotel debe de ser una cadena de carácteres.\n")
           print("Vuelva a introducirlo de nuevo:\n")
           nombre = input()
        self.nombre = nombre
        self.pers = pers
        self.habitaciones = habitaciones
        self.dias = dias
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def getPersones(self):
        return self.pers

    def getDias(self):
        return self.dias

    def getHabitaciones(self):
        return self.habitaciones

    def getNombre(self):
        return self.nombre

    def getId(self):
        return self.id

    def modificarDies(self, dias, precio):
        self.dias = dias
        self.precio = precio

    def modificarHabitaciones(self, habitaciones, precio):
        self.habitaciones = habitaciones
        self.precio = precio

    def modificarPersonas(self, pers, precio):
        self.pers = pers
        self.precio = precio

    def modificarPrecio(self, precio):
        self.precio = precio