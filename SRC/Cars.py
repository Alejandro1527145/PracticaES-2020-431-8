class Cars:

    def __init__(self):
        pass

    def __init__(self, codi, marca, llocRecogida, dies, preu):
        self.codi = codi
        self.marca = marca
        self.llocRecogida = llocRecogida
        self.dies = dies
        self.preu = preu
        self.llista_c = []
        self.llista_c.append(self.codi)
        self.llista_m = []
        self.llista_m.append(self.marca)
        self.llista_r = []
        self.llista_r.append(self.llocRecogida)
        self.llista_d = []
        self.llista_d.append(self.dies)
        self.llista_p = []
        self.llista_p.append(self.preu)

    def getPrecio(self):
        precio = 0
        for i in self.llista_p:
            precio += i
        return precio

    def afegirCotxe(self, codi, marca, llocRecogida, dies, preu):
        self.llista_c.append(codi)
        self.llista_m.append(marca)
        self.llista_r.append(llocRecogida)
        self.llista_d.append(dies)
        self.llista_p.append(preu)
        return self.llista_c, self.llista_m, self.llista_r, self.llista_d, self.llista_p

