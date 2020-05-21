class Hotels:

    def __init__(self):
        pass

    def __init__(self, nombre, dias, pers, habitaciones, id, precio):
        self.id = id
        self.nombre = nombre
        self.pers = pers
        self.habitaciones = habitaciones
        self.dias = dias
        self.precio = precio

    def getPrecio(self):
        return self.precio

