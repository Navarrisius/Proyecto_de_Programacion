import pygame
import noise
import random
import math
ESCALA_RUIDO = 0.01
COLOR_TERRENO = (128, 64, 0)
semilla = random.randint(0, 50)
class Partida:
    en_partida = None
    
    # Al instanciar una partida, se encuentra "corriendo la partida"
    def __init__(self):
        self.en_partida = True

    def cargar_fondo(self, screen):
        mountain_png = pygame.image.load("img/Background/mountain.png").convert_alpha()
        screen.blit(mountain_png, (0, 0))

    def generar_terreno(ANCHO_MUNDO, ALTURA_MUNDO):

        terreno = pygame.Surface((ANCHO_MUNDO, ALTURA_MUNDO))

        for x in range(ANCHO_MUNDO):
        # Determina la altura del terreno en este punto, el primer decimal para aumentar la altura de las montañas , el segundo para aumentar o disminuir el terreno
            altura = int(noise.pnoise1(x * ESCALA_RUIDO, base=semilla) * 0.3 * ALTURA_MUNDO + 0.5 * ALTURA_MUNDO)
        # Rellena el terreno hasta esta altura
            pygame.draw.line(terreno, COLOR_TERRENO, (x, ALTURA_MUNDO), (x, altura), 1)

        return terreno
