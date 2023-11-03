class Bala:
    tipo_bala = None
    dano = None
    radio_bala = None
    unidades = None
    radio_impacto = None
    precio = None

    def __init__(self, tipo):
        # Bala 60 mm
        if tipo == 0:
            self.radio_bala = 6
            self.dano = 30
            self.unidades = 0
            self.radio_impacto = 20
            self.precio = 1000

        # Bala 80 mm
        elif tipo == 1:
            self.radio_bala = 8
            self.dano = 40
            self.unidades = 0
            self.radio_impacto = 30
            self.precio = 2500

        # Bala 105 mm
        elif tipo == 2:
            self.radio_bala = 10
            self.dano = 50
            self.unidades = 0
            self.radio_impacto = 40
            self.precio = 4000