import pygame

class Partida:
    en_partida = None
    
    # Al instanciar una partida, se encuentra "corriendo la partida"
    def __init__(self):
        self.en_partida = True

    def cargar_fondo(self, screen):
        mountain_png = pygame.image.load("img/Background/mountain.png").convert_alpha()
        screen.blit(mountain_png, (0, 0))

    def cargar_terreno():
        pass