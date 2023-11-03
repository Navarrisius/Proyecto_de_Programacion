class Jugador:
    nombre = None
    tanque = None
    puede_jugar = False
    dinero = 10000

    def __init__(self, nombre, tanque):
        self.nombre = nombre
        self.tanque = tanque

    def comprar_bala_60mm(self):
        if self.dinero >= 1000:
            self.tanque.municion[0].unidades += 1
            self.dinero -= 1000
        else:
            print("Dinero insuficiente")

    def comprar_bala_80mm(self):
        if self.dinero >= 2500:
            self.tanque.municion[1].unidades += 1
            self.dinero -= 2500
        else:
            print("Dinero insuficiente")

    def comprar_bala_105mm(self):
        if self.dinero >= 4000:
            self.tanque.municion[2].unidades += 1
            self.dinero -= 4000
        else:
            print("Dinero insuficiente")