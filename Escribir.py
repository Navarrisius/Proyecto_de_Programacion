import pygame
import constantes

class Escribir:
    def escribir_texto(pantalla, texto, fuente, size_fuente, color_fuente, color_fondo, x, y):
        fuente = pygame.font.SysFont(fuente, size_fuente)
        texto = fuente.render(texto, True, color_fuente, color_fondo)
        pantalla.blit(texto, (x, y))


    def render_text(screen, text, posicion, font_size, color, fuente):
        #Obtenemos las dimensiones de la pantalla
        pantalla_ancho, pantalla_alto = constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA
        # Ajustamos el tamaño de la fuente en función del tamaño de la pantalla
        x = posicion[0] * pantalla_ancho
        y = posicion[1] * pantalla_alto
        adjusted_font_size = int(font_size * pantalla_ancho // 800)
        # Creamos la fuente y renderizamos el texto
        fuente = pygame.font.SysFont(fuente, adjusted_font_size)
        text_surface = fuente.render(text, True, color)
        # Obtenemos el rectángulo del texto y lo centramos en la posición especificada
        text_rect = text_surface.get_rect(center=(x,y))
        # Dibujamos el texto en la pantalla
        screen.blit(text_surface, text_rect)
        ##Posicion no se ajusta a tipos de pantalla posible mejora futura