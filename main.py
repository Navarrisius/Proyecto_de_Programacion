import pygame
import math
import clases
from constantes import *


def main():
    # Se inicia Pygame y variables importantes dentro de la ejecución
    pygame.init()
    pygame.display.set_caption(NOMBRE_VENTANA)
    info = pygame.display.Info()
    ANCHO_VENTANA = info.current_w
    ALTO_VENTANA = info.current_h
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE,pygame.OPENGL)
    game = clases.Partida()
    terreno = clases.Terreno()
    fondo = clases.Fondo()
    running = game.en_partida
    reloj = pygame.time.Clock()
    disparo = None
    altura_terreno = [0] * ANCHO_VENTANA
    for x in range(ANCHO_VENTANA):
        altura_terreno[x] += terreno.generar_terreno(x, 200, ALTO_VENTANA)

    while running:
        terreno.dibujar_terreno(pantalla, ANCHO_VENTANA, ALTO_VENTANA)
        reloj = pygame.time.Clock()
        teclas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                NUEVO_ANCHO, NUEVA_ALTURA = event.size
                pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE, pygame.OPENGL)
                ANCHO_VENTANA, ALTO_VENTANA = NUEVO_ANCHO, NUEVA_ALTURA
            elif teclas[pygame.K_ESCAPE]:
                # Cambia la resolución de la ventana y el juego a 1280x720 al presionar la tecla Escape
                ANCHO_VENTANA = 1280
                ALTO_VENTANA = 720
                pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE, pygame.OPENGL)
            if jugador_1.puede_jugar:
                # Verifica si la tecla 'A' se mantiene presionada
                if teclas[pygame.K_a]:
                    jugador_1.tanque.angulo_n += 0.5
                    if jugador_1.tanque.angulo_n > limite_angulo_max:
                        jugador_1.tanque.angulo_n = limite_angulo_max
                    jugador_1.tanque.angulo_canon = math.radians(jugador_1.tanque.angulo_n)
                if teclas[pygame.K_a] and teclas[pygame.K_LSHIFT]:
                    jugador_1.tanque.angulo_n += 1.5
                    if jugador_1.tanque.angulo_n > limite_angulo_max:
                        jugador_1.tanque.angulo_n = limite_angulo_max
                    jugador_1.tanque.angulo_canon = math.radians(jugador_1.tanque.angulo_n) 
                # Verifica si la tecla 'D' se mantiene presionada
                if teclas[pygame.K_d]:
                    jugador_1.tanque.angulo_n -= 0.5
                    if jugador_1.tanque.angulo_n < limite_angulo_min:
                        jugador_1.tanque.angulo_n = limite_angulo_min
                    jugador_1.tanque.angulo_canon = math.radians(jugador_1.tanque.angulo_n)
                if teclas[pygame.K_d] and teclas[pygame.K_LSHIFT]:
                    jugador_1.tanque.angulo_n -= 1.5
                    if jugador_1.tanque.angulo_n < limite_angulo_min:
                        jugador_1.tanque.angulo_n = limite_angulo_min
                    jugador_1.tanque.angulo_canon = math.radians(jugador_1.tanque.angulo_n)    
                # Verifica si la tecla 'W' se mantiene presionada
                if teclas[pygame.K_w]:
                    jugador_1.tanque.velocidad_disparo += 1.5
                if teclas[pygame.K_w] and teclas[pygame.K_LSHIFT]:
                    jugador_1.tanque.velocidad_disparo += 3.0
                # Verifica si la tecla 'S' se mantiene presionada
                if teclas[pygame.K_s]:
                    jugador_1.tanque.velocidad_disparo -= 1.5
                    if jugador_1.tanque.velocidad_disparo < limite_velocidad_min:
                        jugador_1.tanque.velocidad_disparo = limite_velocidad_min
                if teclas[pygame.K_s] and teclas[pygame.K_LSHIFT]:
                    jugador_1.tanque.velocidad_disparo -= 3.0
                    if jugador_1.tanque.velocidad_disparo < limite_velocidad_min:
                        jugador_1.tanque.velocidad_disparo = limite_velocidad_min
                # Verifica disparo del tanque y cambio de turnos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #Disparo
                        #Se intancia el disparo
                        disparo = clases.Disparo(jugador_1.tanque.angulo_n, jugador_1.tanque.velocidad_disparo, jugador_1.tanque)
                        if jugador_1.tanque.disparar(pantalla=pantalla, terreno=terreno, ancho=ANCHO_VENTANA, alto=ALTO_VENTANA,disparo=disparo, altura_terreno=altura_terreno, tanque_enemigo=jugador_2.tanque):
                            game.ganador = jugador_1
                            jugador_2.puede_jugar = False
                            jugador_1.puede_jugar = False
                        else:
                            #Cambia turnos
                            jugador_2.puede_jugar = True
                            jugador_1.puede_jugar = False
                        break

            if jugador_2.puede_jugar:
                # Verifica si la tecla 'A' se mantiene presionada
                if teclas[pygame.K_a]:
                    jugador_2.tanque.angulo_n += 0.5
                    if jugador_2.tanque.angulo_n > limite_angulo_max:
                        jugador_2.tanque.angulo_n = limite_angulo_max
                    jugador_2.tanque.angulo_canon = math.radians(jugador_2.tanque.angulo_n)
                if teclas[pygame.K_a] and teclas[pygame.K_LSHIFT]:
                    jugador_2.tanque.angulo_n += 1.5
                    if jugador_2.tanque.angulo_n > limite_angulo_max:
                        jugador_2.tanque.angulo_n = limite_angulo_max
                    jugador_2.tanque.angulo_canon = math.radians(jugador_2.tanque.angulo_n) 
                # Verifica si la tecla 'D' se mantiene presionada
                if teclas[pygame.K_d]:
                    jugador_2.tanque.angulo_n -= 0.5
                    if jugador_2.tanque.angulo_n < limite_angulo_min:
                        jugador_2.tanque.angulo_n = limite_angulo_min
                    jugador_2.tanque.angulo_canon = math.radians(jugador_2.tanque.angulo_n)
                if teclas[pygame.K_d] and teclas[pygame.K_LSHIFT]:
                    jugador_2.tanque.angulo_n -= 1.5
                    if jugador_2.tanque.angulo_n < limite_angulo_min:
                        jugador_2.tanque.angulo_n = limite_angulo_min
                    jugador_2.tanque.angulo_canon = math.radians(jugador_2.tanque.angulo_n)    
                # Verifica si la tecla 'W' se mantiene presionada
                if teclas[pygame.K_w]:
                    jugador_2.tanque.velocidad_disparo += 1.5
                if teclas[pygame.K_w] and teclas[pygame.K_LSHIFT]:
                    jugador_2.tanque.velocidad_disparo += 3.0
                # Verifica si la tecla 'S' se mantiene presionada
                if teclas[pygame.K_s]:
                    jugador_2.tanque.velocidad_disparo -= 1.5
                    if jugador_2.tanque.velocidad_disparo < limite_velocidad_min:
                        jugador_2.tanque.velocidad_disparo = limite_velocidad_min
                if teclas[pygame.K_s] and teclas[pygame.K_LSHIFT]:
                    jugador_2.tanque.velocidad_disparo -= 3.0
                    if jugador_2.tanque.velocidad_disparo < limite_velocidad_min:
                        jugador_2.tanque.velocidad_disparo = limite_velocidad_min
                # Verifica disparo del tanque y cambio de turnos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #Disparo
                        #Se intancia el disparo
                        disparo = clases.Disparo(jugador_2.tanque.angulo_n, jugador_2.tanque.velocidad_disparo, jugador_2.tanque)        
                        if jugador_2.tanque.disparar(pantalla=pantalla, terreno=terreno, ancho=ANCHO_VENTANA, alto=ALTO_VENTANA,disparo=disparo, altura_terreno=altura_terreno, tanque_enemigo=jugador_1.tanque):
                            game.ganador = jugador_2
                            jugador_2.puede_jugar = False
                            jugador_1.puede_jugar = False
                        else:
                            #Cambia turnos
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


        # Se escribe en pantalla la información del pre-disparo de cada jugador
        if jugador_1.puede_jugar == True:
            Escribir.escribir_texto(pantalla=pantalla, texto="Ángulo: " + str(jugador_1.tanque.angulo_n) + "°", color_fuente=(255, 255, 255), fuente="Consolas", size_fuente=20,color_fondo=jugador_1.tanque.color, x=jugador_1.tanque.posicion_x + 30, y=jugador_1.tanque.posicion_y)
            Escribir.escribir_texto(pantalla=pantalla, texto="Velocidad Inicial: " + str(jugador_1.tanque.velocidad_disparo) + " m/s", fuente="Consolas", color_fuente=(255, 255, 255), size_fuente=20,color_fondo=jugador_1.tanque.color, x=jugador_1.tanque.posicion_x + 30, y=jugador_1.tanque.posicion_y + 20)
        elif jugador_2.puede_jugar == True:
            Escribir.escribir_texto(pantalla=pantalla, texto="Ángulo: " + str(jugador_2.tanque.angulo_n) + "°", color_fuente=(255, 255, 255), fuente="Consolas", size_fuente=20, color_fondo=jugador_2.tanque.color, x=jugador_2.tanque.posicion_x - 180, y=jugador_2.tanque.posicion_y)
            Escribir.escribir_texto(pantalla=pantalla, texto="Velocidad Inicial: " + str(jugador_2.tanque.velocidad_disparo) + " m/s", fuente="Consolas", color_fuente=(255, 255, 255), size_fuente=20, color_fondo=jugador_2.tanque.color, x=jugador_2.tanque.posicion_x - 180, y=jugador_2.tanque.posicion_y + 20)

        # Texto con el jugador ganador
        if game.ganador != None:
            disparo.recorrido(pantalla)
            if game.ganador == jugador_1:
                Escribir.escribir_texto(pantalla=pantalla, texto="Ganador: Jugador 1", fuente="Arial", size_fuente=35, color_fuente=(255, 255, 255), color_fondo=jugador_1.tanque.color, x=ANCHO_VENTANA // 2.5, y=ALTO_VENTANA // 2)
            else:
                Escribir.escribir_texto(pantalla=pantalla, texto="Ganador: Jugador 2", fuente="Arial", size_fuente=35, color_fuente=(255, 255, 255), color_fondo=jugador_2.tanque.color, x=ANCHO_VENTANA // 2.5, y=ALTO_VENTANA // 2)
            
            pygame.display.update()

            # Esperar 5 segundos antes de cerrar la ventana
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_espera = 5000
            while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                None
            running = False
            disparo = None         
        else:
            jugador_1.tanque.draw_tank(pantalla)
            jugador_2.tanque.draw_tank(pantalla)

        if disparo != None:
            disparo.recorrido(pantalla)
            Escribir.escribir_texto(pantalla=pantalla, texto="Altura máxima: " + str(int(disparo.altura_maxima)) + " m.", color_fuente=(255, 255, 255), fuente="Arial", size_fuente=25,color_fondo=(0,0,0), x=ANCHO_VENTANA // 2, y=ALTO_VENTANA // 3)
            if disparo.distancia_maxima != -1:
                Escribir.escribir_texto(pantalla=pantalla, texto="Distancia máxima: " + str(int(disparo.distancia_maxima)) + " m.", color_fuente=(255, 255, 255), fuente="Arial", size_fuente=25,color_fondo=(0,0,0), x=ANCHO_VENTANA // 2, y=ALTO_VENTANA // 3 + 28)
            else:
                Escribir.escribir_texto(pantalla=pantalla, texto="Disparo fuera del mapa", color_fuente=(255, 255, 255), fuente="Arial", size_fuente=25,color_fondo=(0,0,0), x=ANCHO_VENTANA // 2, y=ALTO_VENTANA // 3 + 28)
            pygame.display.update()

            # Esperar 2 segundos
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_espera = 2000
            while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                None
            disparo = None


        pygame.display.flip()

        # Limita los FPS a 60
        reloj.tick(60)

    pygame.quit()

main()