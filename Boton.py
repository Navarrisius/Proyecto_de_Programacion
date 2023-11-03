import pygame

import constantes


class Boton:
    def __init__(self, x, y, ancho, alto, text, color, hover_color, color_texto):
        self.x_ratio = x / constantes.ANCHO_VENTANA
        self.y_ratio = y / constantes.ALTO_VENTANA
        self.width_ratio = ancho / constantes.ALTO_VENTANA
        self.height_ratio = alto / constantes.ANCHO_VENTANA
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.color_texto = color_texto

    def dibujar(self, surface, ancho, alto):
        x = self.x_ratio * ancho
        y = self.y_ratio * alto
        w = self.width_ratio * ancho
        h = self.height_ratio * alto

        mouse_pos = pygame.mouse.get_pos()

        if x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h:
            pygame.draw.rect(surface, self.hover_color, (x, y, w, h))
        else:
            pygame.draw.rect(surface, self.color, (x, y, w, h))

        font = pygame.font.Font(None, int(h // 1.5))
        text_surf = font.render(self.text, True, self.color_texto)
        text_rect = text_surf.get_rect(center=(x + w // 2, y + h // 2))
        surface.blit(text_surf, text_rect)

    def si_clic(self, ancho, alto):
        x = self.x_ratio * ancho
        y = self.y_ratio * alto
        w = self.width_ratio * ancho
        h = self.height_ratio * alto

        mouse_pos = pygame.mouse.get_pos()
        return x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h