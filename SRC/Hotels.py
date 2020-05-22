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

    def modificarRHotel(self, dias = self.dias, pers = self.pers, habitaciones = self.habitaciones):
        print("¿Que desea cambiar sobre su reserva?")
        print(" 1: DIAS \n 2: NÚMERO DE HOSTS \n 3: HABITACIÓN")

        case = input()
        while((case < 0 ) || (case > 3))
            print("Error: Vuelva a introducir los datos...")
            case = input()
        if case == 1:
            print("Introduzca el número de dias que desea estar")
            correcto == False
            while(correcto == False)
            dias = input()
            if(dias <= 0):
                print("El número de días debe de ser almenos 1")



