
import pygame
import noise
import random
import math
import clases
from constantes import *



def generar_terreno(x, altura_maxima, width):
    return altura_maxima * math.e ** (-((x - width) ** 2) / (2 * (width / 2) ** 2)) * math.cos(0.01 * (x - width)) + 200
def main():
    ANCHO_VENTANA = 1280
    ALTO_VENTANA = 768
    NOMBRE_VENTANA = "Juego XD"
    ANCHO_MUNDO = math.ceil(ANCHO_VENTANA/1.5)
    ALTURA_MUNDO = math.ceil(ALTO_VENTANA/1.5)
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE,pygame.OPENGL)
    game = clases.Partida()
    altura_terreno = [0] * ANCHO_VENTANA
    for x in range(ANCHO_VENTANA):
        altura_terreno[x] += generar_terreno(x, 200, ALTO_VENTANA)
    running = game.en_partida
    reloj = pygame.time.Clock()

    # Se inicia Pygame y se cambia el título de la ventana
    pygame.init()
    pygame.display.set_caption(NOMBRE_VENTANA)

    #Texto
    def escribir_texto(pantalla, texto, color_fuente, color_fondo, x, y):
        fuente = pygame.font.SysFont("consolas", 18)
        texto = fuente.render(texto, True, color_fuente, color_fondo)
        pantalla.blit(texto, (x, y))

    while running:
        # Captura todos los eventos dentro del juego
        for event in pygame.event.get():
            # Captura el cierre de la ventana
            if event.type == pygame.QUIT:
                running = False
            # Captura eventos de cambio de tamaño de ventana
            if event.type == pygame.VIDEORESIZE: 
                NUEVO_ANCHO, NUEVA_ALTURA = event.size
                # Cambia el tamaño de la ventana
                pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE,pygame.OPENGL)
            teclas = pygame.key.get_pressed()

            if jugador_1.puede_jugar:
                # Verifica si la tecla 'A' se mantiene presionada
                if teclas[pygame.K_a]:
                    jugador_1.tanque.angulo_n += 0.5
                    if jugador_1.tanque.angulo_n > limite_angulo_max:
                        jugador_1.tanque.angulo_n = limite_angulo_max
                    jugador_1.tanque.angulo_canon = math.radians(jugador_1.tanque.angulo_n)

                # Verifica si la tecla 'D' se mantiene presionada
                if teclas[pygame.K_d]:
                    tecla_d_pulsada = True
                    jugador_1.tanque.angulo_n -= 0.5
                    if jugador_1.tanque.angulo_n < limite_angulo_min:
                        jugador_1.tanque.angulo_n = limite_angulo_min
                    jugador_1.tanque.angulo_canon = math.radians(jugador_1.tanque.angulo_n)
                # Verifica disparo del tanque y cambio de turnos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #Disparo
                        jugador_2.puede_jugar = True
                        jugador_1.puede_jugar = False
                        break

            if jugador_2.puede_jugar:

                if teclas[pygame.K_a]:
                    jugador_2.tanque.angulo_n += 0.5
                    if jugador_2.tanque.angulo_n > limite_angulo_max:
                        jugador_2.tanque.angulo_n = limite_angulo_max
                    jugador_2.tanque.angulo_canon = math.radians(jugador_2.tanque.angulo_n)

                if teclas[pygame.K_d]:
                    jugador_2.tanque.angulo_n -= 0.5
                    if jugador_2.tanque.angulo_n < limite_angulo_min:
                        jugador_2.tanque.angulo_n = limite_angulo_min
                    jugador_2.tanque.angulo_canon = math.radians(jugador_2.tanque.angulo_n)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jugador_2.puede_jugar = False
                        jugador_1.puede_jugar = True
                        break

        #VACIA PANTALLA
        pantalla.fill((0, 0, 0))

        # Mantener el tanque en el terreno
        jugador_1.tanque.posicion_y = ALTO_VENTANA - altura_terreno[jugador_1.tanque.posicion_x]
        jugador_2.tanque.posicion_y = ALTO_VENTANA - altura_terreno[jugador_2.tanque.posicion_x]



        #terreno
        for x in range(ANCHO_VENTANA):
            pygame.draw.rect(pantalla, (0, 255, 0), (x, ALTO_VENTANA - altura_terreno[x], 1, altura_terreno[x]))

        #escribir_texto(pantalla=pantalla, texto="Ángulo: " + str(angulo_n) + "°", color_fuente=(255, 255, 255), color_fondo=(0, 0, 255), x=tanque_1.posicion_x + 100, y=tanque_1.posicion_y)
        def draw_tank(screen, tanque):
            tank_points = [(tanque.posicion_x - 50 // 2, tanque.posicion_y),(tanque.posicion_x - 50 // 2, tanque.posicion_y - 10),
                           (tanque.posicion_x - 50 // 2 + 5, tanque.posicion_y - 13),(tanque.posicion_x + 50 // 2 - 5, tanque.posicion_y - 13),
                           (tanque.posicion_x + 50 // 2, tanque.posicion_y - 10),(tanque.posicion_x + 50 // 2, tanque.posicion_y)]
            pygame.draw.polygon(screen, tanque.color, tank_points)
            # Dibuja la torreta del tanque
            turret_length = 30
            turret_start = (tanque.posicion_x, tanque.posicion_y - 10)
            turret_end = (tanque.posicion_x + turret_length * math.cos(tanque.angulo_canon),tanque.posicion_y - 10 - turret_length * math.sin(tanque.angulo_canon))
            pygame.draw.line(screen, "gray", turret_start, turret_end, 4)
        #Agregar tanque
        draw_tank(pantalla, jugador_1.tanque)
        draw_tank(pantalla, jugador_2.tanque)
        #pygame.draw.rect(pantalla,(0, 255, 0), (tanque_1.posicion_x, tanque_1.posicion_y, 50, 30))
        #pygame.draw.line(pantalla, (150, 150, 150),(tanque_1.posicion_x, tanque_1.posicion_y), (x1, y1), 10)

        pygame.display.flip()
        # Limita los FPS a 60
        reloj.tick(60)

    pygame.quit()

main()