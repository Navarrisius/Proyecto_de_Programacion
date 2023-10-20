import pygame

class Fondo:
    mountain_png = None
    fondo_terreno = None

    def __init__(self):
        self.mountain_png = pygame.image.load("img/mountain.png").convert_alpha()

    def cargar_fondo(self, screen, tipo):
        if tipo == 1:
            screen.blit(self.mountain_png, (0, 0))