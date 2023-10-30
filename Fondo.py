import pygame
import constantes

class Fondo:
    mountain_png = None
    fondo_terreno = None

    def __init__(self):
        self.mountain_png = pygame.image.load("img/mountain.png").convert_alpha()

    def cargar_fondo(self, screen, tipo):
        self.mountain_png = pygame.transform.scale(self.mountain_png, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
        screen.blit(self.mountain_png, (0, 0))