import pygame
import constantes
import funciones

def main():
    # Se inicia Pygame y variables importantes dentro de la ejecución
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('mp3/aria_math.mp3')
    pygame.mixer.music.set_volume(0.02)
    pygame.mixer.music.play(-1)
    img_ventana = pygame.image.load('img/pessi.png')
    pygame.display.set_icon(img_ventana)
    pygame.display.set_caption(constantes.NOMBRE_VENTANA)
    funciones.actualizar_info_pantalla()
    #constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA = 800, 800
    constantes.PANTALLA = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA), pygame.RESIZABLE,
                                       pygame.OPENGL)
    game = funciones.Partida()
    funciones.menu(constantes.PANTALLA, game)
    pygame.quit()

main()