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
    tanque_1 = clases.Tanque("red")
    gravedad = 1
    tanque_1.posicion_x = 30
    tanque_1.posicion_y = 30
    radio = 30
    angulo_n = 0

    while running:
        # Captura todos los eventos dentro del juego
        for event in pygame.event.get():
            # Captura el cierre de la ventana
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE: # Captura eventos de cambio de tamaño de ventana
                NUEVO_ANCHO, NUEVA_ALTURA = event.size
                pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE,pygame.OPENGL)# Cambia el tamaño de la ventana
            if event.type == pygame.KEYDOWN:
                # JUGADOR 1
                if event.key == pygame.K_d:
                    angulo_n += 1
                if event.key == pygame.K_a:
                    angulo_n -= 1

        angulo = (math.radians(angulo_n))
        x1 = tanque_1.posicion_x + 40 * math.sin(angulo)
        y1 = tanque_1.posicion_y - 40 * math.cos(angulo)

        terreno_escalado = pygame.transform.scale(textura_terreno, (pantalla.get_width(), pantalla.get_height()))
        pantalla.blit(terreno_escalado, (0, 0))

        #Agregar tanque
        pygame.draw.rect(pantalla,(0, 255, 0), (tanque_1.posicion_x, tanque_1.posicion_y, 50, 30))
        pygame.draw.line(pantalla, (150, 150, 150),(tanque_1.posicion_x, tanque_1.posicion_y), (x1, y1), 10)
        print(angulo, "-", x1)
        if(tanque_1.posicion_y == ALTURA_TERRENO[tanque_1.posicion_x] + 100):
            tanque_1.posicion_y += 0
        else:
            tanque_1.posicion_y += gravedad

        pygame.display.flip()
        # Limita los FPS a 60
        reloj.tick(60)

    pygame.quit()

main()