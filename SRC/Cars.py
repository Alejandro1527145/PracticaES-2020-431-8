class Cars:

    def __init__(self):
        pass

    def __init__(self, codi, marca, llocRecogida, dies, preu):
        self.codi = codi
        self.marca = marca
        self.llocRecogida = llocRecogida
        self.dies = dies
        self.preu = preu

    def getPrecio(self):
        return self.preu
