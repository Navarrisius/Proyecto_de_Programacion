class Bala:
    tipo_bala = None
    dano = None
    radio_bala = None
    unidades = None
    radio_impacto = None
    costo = None

    def __init__(self, tipo):
        if tipo == 0:
            self.radio_bala = 6
            self.dano = 30
            self.unidades = 3
            self.radio_impacto = 20
        elif tipo == 1:
            self.radio_bala = 8
            self.dano = 40
            self.unidades = 10
            self.radio_impacto = 30
        elif tipo == 2:
            self.radio_bala = 10
            self.dano = 50
            self.unidades = 3
            self.radio_impacto = 40