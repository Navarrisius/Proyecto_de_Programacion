import pygame
import noise
import random
import math


class Disparo:
    angulo = None
    velocidad_inicial = None
    altura_maxima = None
    distancia_recorrida = None

    def __init__(self, angulo, velocidad_inicial):
        self.angulo = angulo
        self.velocidad_inicial = velocidad_inicial

class Jugador:
    nombre = None
    tanque = None
    puede_jugar = False

    def __init__(self, nombre, tanque):
        self.nombre = nombre
        self.tanque = tanque



class Partida:
    en_partida = None
    def __init__(self):
        self.en_partida = True

    def cargar_fondo(self, screen):
        mountain_png = pygame.image.load("img/Background/mountain.png").convert_alpha()
        screen.blit(mountain_png, (0, 0))

    def generar_terreno(self, ANCHO_MUNDO, ALTURA_MUNDO):
        ESCALA_RUIDO = 0.01
        COLOR_TERRENO = (128, 64, 0)
        semilla = random.randint(0, 50)
        terreno = pygame.Surface((ANCHO_MUNDO, ALTURA_MUNDO))
        for x in range(ANCHO_MUNDO):
        # Determina la altura del terreno en este punto, el primer decimal para aumentar la altura de las montañas , el segundo para aumentar o disminuir el terreno
            altura = int(noise.pnoise1(x * ESCALA_RUIDO, base=semilla) * 0.4 * ALTURA_MUNDO + 0.6 * ALTURA_MUNDO)
        # Rellena el terreno hasta esta altura
            pygame.draw.line(terreno, COLOR_TERRENO, (x, ALTURA_MUNDO), (x, altura), 1)
        return terreno
    
class Tanque:
    color = None
    posicion_x = None
    posicion_y = None
    vivo = True

    def __init__(self, color):
        self.color = color