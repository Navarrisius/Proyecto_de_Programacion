import pygame
import math
import clases
from Constantes_Variables import *


def main():
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE,pygame.OPENGL)
    game = clases.Partida()
    terreno = clases.Terreno()
    fondo = clases.Fondo()
    running = game.en_partida
    reloj = pygame.time.Clock()
    altura_terreno = [0] * ANCHO_VENTANA
    for x in range(ANCHO_VENTANA):
        altura_terreno[x] += terreno.generar_terreno(x, 200, ALTO_VENTANA)

    # Se inicia Pygame y se cambia el título de la ventana
    pygame.init()
    pygame.display.set_caption(NOMBRE_VENTANA)

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
                    jugador_1.tanque.angulo_n -= 0.5
                    if jugador_1.tanque.angulo_n < limite_angulo_min:
                        jugador_1.tanque.angulo_n = limite_angulo_min
                    jugador_1.tanque.angulo_canon = math.radians(jugador_1.tanque.angulo_n)
                # Verifica si la tecla 'FLECHA DERECHA' se mantiene presionada
                if teclas[pygame.K_RIGHT]:
                    jugador_1.tanque.velocidad_disparo += 1.5
                # Verifica si la tecla 'FLECHA IZQUIERDA' se mantiene presionada
                if teclas[pygame.K_LEFT]:
                    jugador_1.tanque.velocidad_disparo -= 1.5
                # Verifica disparo del tanque y cambio de turnos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #Disparo
                        #Se intancia el disparo
                        disparo = clases.Disparo(jugador_1.tanque.angulo_n, jugador_1.tanque.velocidad_disparo)        
                        if jugador_1.tanque.disparar(pantalla=pantalla, terreno=terreno, ancho=ANCHO_VENTANA, alto=ALTO_VENTANA,disparo=disparo, altura_terreno=altura_terreno, tanque_enemigo=jugador_2.tanque):
                            Escribir.escribir_texto(pantalla=pantalla, texto="GANADOR JUGADOR 1", color_fuente=(255, 255, 255), color_fondo=jugador_1.tanque.color, x=ANCHO_VENTANA // 2, y=ALTO_VENTANA // 2)
                            pygame.time.delay(3000)
                            running = False
                        else:
                            #Cambia turnos
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
                # Verifica si la tecla 'FLECHA DERECHA' se mantiene presionada
                if teclas[pygame.K_RIGHT]:
                    jugador_2.tanque.velocidad_disparo += 1.5
                # Verifica si la tecla 'FLECHA IZQUIERDA' se mantiene presionada
                if teclas[pygame.K_LEFT]:
                    jugador_2.tanque.velocidad_disparo -= 1.5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        disparo = clases.Disparo(jugador_2.tanque.angulo_n, jugador_2.tanque.velocidad_disparo)
                        if jugador_2.tanque.disparar(pantalla=pantalla, terreno=terreno, ancho=ANCHO_VENTANA, alto=ALTO_VENTANA,disparo=disparo, altura_terreno=altura_terreno, tanque_enemigo=jugador_1.tanque):
                            Escribir.escribir_texto(pantalla=pantalla, texto="GANADOR JUGADOR 2", color_fuente=(255, 255, 255), color_fondo=jugador_2.tanque.color, x=ANCHO_VENTANA // 2, y=ALTO_VENTANA // 2)
                            pygame.time.delay(3000)
                            running = False
                        else:
                            jugador_2.puede_jugar = False
                            jugador_1.puede_jugar = True
                        break

        #VACIA PANTALLA
        fondo.cargar_fondo(pantalla)

        # Mantener el tanque en el terreno
        jugador_1.tanque.posicion_y = ALTO_VENTANA - altura_terreno[jugador_1.tanque.posicion_x]
        jugador_2.tanque.posicion_y = ALTO_VENTANA - altura_terreno[jugador_2.tanque.posicion_x]


        #Terreno
        terreno.dibujar_terreno(pantalla=pantalla, ancho=ANCHO_VENTANA, alto=ALTO_VENTANA)

        # Se escribe en pantalla la información del disparo de cada jugador
        if jugador_1.puede_jugar == True:
            Escribir.escribir_texto(pantalla=pantalla, texto="Ángulo: " + str(jugador_1.tanque.angulo_n) + "°" + " | Velocidad Inicial: " + str(jugador_1.tanque.velocidad_disparo), color_fuente=(255, 255, 255), color_fondo=jugador_1.tanque.color, x=jugador_1.tanque.posicion_x + 10, y=jugador_1.tanque.posicion_y)
        else:
            Escribir.escribir_texto(pantalla=pantalla, texto="Ángulo: " + str(jugador_2.tanque.angulo_n) + "°" + " | Velocidad Inicial: " + str(jugador_2.tanque.velocidad_disparo), color_fuente=(255, 255, 255), color_fondo=jugador_2.tanque.color, x=jugador_2.tanque.posicion_x + 10, y=jugador_2.tanque.posicion_y + 10)

        jugador_1.tanque.draw_tank(pantalla)
        jugador_2.tanque.draw_tank(pantalla)
        pygame.display.flip()
        # Limita los FPS a 60
        reloj.tick(60)

    pygame.quit()

main()