import pygame

class Escribir:
    def escribir_texto(pantalla, texto, fuente, size_fuente, color_fuente, color_fondo, x, y):
        fuente = pygame.font.SysFont(fuente, size_fuente)
        texto = fuente.render(texto, True, color_fuente, color_fondo)
        pantalla.blit(texto, (x, y))