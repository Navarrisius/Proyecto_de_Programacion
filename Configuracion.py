class Configuracion:
    num_jugadores = None
    ancho_pantalla = None
    alto_pantalla = None
    num_partidas = None

    def __init__(self, num_jugadores, ancho_pantalla, alto_pantalla, num_partidas):
        self.num_jugadores = num_jugadores
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
        self.num_partidas = num_partidas
        