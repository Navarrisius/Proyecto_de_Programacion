import pygame
import noise
import random
import math
import clases

def main():
    ANCHO_VENTANA = 1280
    ALTO_VENTANA = 768
    NOMBRE_VENTANA = "Juego XD"
    ANCHO_MUNDO = math.ceil(ANCHO_VENTANA/1.5)
    ALTURA_MUNDO = math.ceil(ALTO_VENTANA/1.5)
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE,pygame.OPENGL)
    game = clases.Partida()
    textura_terreno, ALTURA_TERRENO = game.generar_terreno(ANCHO_MUNDO, ALTURA_MUNDO)
    running = game.en_partida
    reloj = pygame.time.Clock()

    # Se inicia Pygame y se cambia el título de la ventana
    pygame.init()
    pygame.display.set_caption(NOMBRE_VENTANA)

    #Seting tanque
    gravedad = 1
    tanque_x = 30
    tanque_y = 30

    while running:
        # Captura todos los eventos dentro del juego
        for event in pygame.event.get():
            # Captura el cierre de la ventana
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE: # Captura eventos de cambio de tamaño de ventana
                NUEVO_ANCHO, NUEVA_ALTURA = event.size
                pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE,pygame.OPENGL)# Cambia el tamaño de la ventana

        terreno_escalado = pygame.transform.scale(textura_terreno, (pantalla.get_width(), pantalla.get_height()))
        pantalla.blit(terreno_escalado, (0, 0))

        #Agregar tanque
        pygame.draw.rect(pantalla,(0, 255, 0), (tanque_x, tanque_y, 50, 30))
        if(tanque_y == ALTURA_TERRENO[tanque_x] + 70):
            tanque_y += 0
        else:
            tanque_y += gravedad

        pygame.display.flip()

        # Limita los FPS a 60
        reloj.tick(60)

    pygame.quit()

main()