class Jugador:
    nombre = None
    tanque = None
    puede_jugar = False
    vivo = True
    dinero = None
    ya_jugado = False
    kills = None

    def __init__(self, nombre, tanque):
        self.nombre = nombre
        self.tanque = tanque
        self.dinero = 10000
        self.kills = 0

    def comprar_bala_60mm(self):
        self.tanque.municion[0].unidades += 1
        self.dinero -= 1000

    def comprar_bala_80mm(self):
        self.tanque.municion[1].unidades += 1
        self.dinero -= 2500

    def comprar_bala_105mm(self):
        self.tanque.municion[2].unidades += 1
        self.dinero -= 4000

    def vender_bala_60mm(self):
        self.tanque.municion[0].unidades -= 1
        self.dinero += 1000

    def vender_bala_80mm(self):
        self.tanque.municion[1].unidades -= 1
        self.dinero += 2500

    def vender_bala_105mm(self):
        self.tanque.municion[2].unidades -= 1
        self.dinero += 4000