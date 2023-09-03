class Disparo:
    angulo = None
    velocidad_inicial = None
    altura_maxima = None
    distancia_recorrida = None

    def __init__(self, angulo, velocidad_inicial):
        self.angulo = angulo
        self.velocidad_inicial = velocidad_inicial