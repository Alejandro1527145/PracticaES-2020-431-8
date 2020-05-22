class Hotels:

    def __init__(self, nombre, dias, pers, habitaciones, id, precio):
        self.id = id
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


