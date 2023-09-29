import pygame
import math
import clases
import constantes
import random


def actualizar_info_pantalla():
    info = pygame.display.Info()
    constantes.ANCHO_VENTANA = info.current_w
    constantes.ALTO_VENTANA = info.current_h


def crear_jugadores():
    colores_rgb = {
        "purpura": (99, 11, 87),
        "rojo": (255, 0, 0),
        "azul": (0, 0, 255),
        "verde_musgo": (47, 69, 56),
        "NEGRO": (0, 0, 0)
    }
    colores_disponibles = list(colores_rgb.values())
    primer_color = random.choice(colores_disponibles)
    colores_disponibles.remove(primer_color)
    segundo_color = random.choice(colores_disponibles)
    colores_disponibles.remove(segundo_color)

    # Se crea el jugador 1
    jugador_1 = clases.Jugador(None, clases.Tanque(primer_color))
    jugador_1.tanque.posicion_x = random.randint(30, constantes.ANCHO_VENTANA // 2 - 100)
    jugador_1.tanque.posicion_y = 30
    jugador_1.tanque.angulo_n = 0
    jugador_1.tanque.angulo_canon = (math.radians(jugador_1.tanque.angulo_n))

    # Se crea el jugador 2
    jugador_2 = clases.Jugador(None, clases.Tanque(segundo_color))
    jugador_2.tanque.posicion_x = random.randint(constantes.ANCHO_VENTANA // 2 + 100, constantes.ANCHO_VENTANA - 50)
    jugador_2.tanque.posicion_y = 30
    jugador_2.tanque.angulo_n = 0
    jugador_2.tanque.angulo_canon = (math.radians(jugador_2.tanque.angulo_n))
    if random.choice([True, False]):
        jugador_1.puede_jugar = True
        jugador_2.puede_jugar = False
    else:
        jugador_1.puede_jugar = True
        jugador_2.puede_jugar = False

    constantes.JUGADORES = [jugador_1, jugador_2]


def cambiar_turnos(jugador1, jugador2):
    if jugador1.puede_jugar:
        jugador1.puede_jugar = False
        jugador2.puede_jugar = True
    else:
        jugador1.puede_jugar = True
        jugador2.puede_jugar = False


def terminar_turnos(jugadores):
    for jugador in jugadores:
        jugador.puede_jugar = False


def main():
    # Se inicia Pygame y variables importantes dentro de la ejecución
    pygame.init()
    pygame.display.set_caption(constantes.NOMBRE_VENTANA)
    actualizar_info_pantalla()
    pantalla = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA), pygame.RESIZABLE,
                                       pygame.OPENGL)
    game = clases.Partida()
    # Joystick
    pygame.joystick.init()
    crear_jugadores()
    jugador_1 = constantes.JUGADORES[0]
    jugador_2 = constantes.JUGADORES[1]
    mandos = []
    terreno = clases.Terreno()
    fondo = clases.Fondo()
    running = game.en_partida
    pygame.time.Clock()
    disparo = None
    UI = clases.UI()
    altura_terreno = [0] * constantes.ANCHO_VENTANA
    for x in range(constantes.ANCHO_VENTANA):
        altura_terreno[x] += terreno.generar_terreno(x, 200, constantes.ALTO_VENTANA)

    while running:
        terreno.dibujar_terreno(pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
        reloj = pygame.time.Clock()
        teclas = pygame.key.get_pressed()
        if jugador_1.puede_jugar:
            turno = jugador_1
            enemigo = jugador_2.tanque
        else:
            turno = jugador_2
            enemigo = jugador_1.tanque
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                mandos.append(joy)
            elif event.type == pygame.VIDEORESIZE:
                NUEVO_ANCHO, NUEVA_ALTURA = event.size
                pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE, pygame.OPENGL)
                constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA = NUEVO_ANCHO, NUEVA_ALTURA
            elif teclas[pygame.K_ESCAPE]:
                running = False
            if teclas[pygame.K_a]:
                turno.tanque.angulo_n += 0.5
                if turno.tanque.angulo_n > constantes.LIMITE_ANGULO_MAX:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MAX
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            if teclas[pygame.K_a] and teclas[pygame.K_LSHIFT]:
                turno.tanque.angulo_n += 1.5
                if turno.tanque.angulo_n > constantes.LIMITE_ANGULO_MAX:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MAX
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            # Verifica si la tecla 'D' se mantiene presionada
            if teclas[pygame.K_d]:
                turno.tanque.angulo_n -= 0.5
                if turno.tanque.angulo_n < constantes.LIMITE_ANGULO_MIN:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MIN
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            if teclas[pygame.K_d] and teclas[pygame.K_LSHIFT]:
                turno.tanque.angulo_n -= 1.5
                if turno.tanque.angulo_n < constantes.LIMITE_ANGULO_MIN:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MIN
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            # Verifica si la tecla 'W' se mantiene presionada
            if teclas[pygame.K_w]:
                turno.tanque.velocidad_disparo += 1.5
            if teclas[pygame.K_w] and teclas[pygame.K_LSHIFT]:
                turno.tanque.velocidad_disparo += 3.0
            # Verifica si la tecla 'S' se mantiene presionada
            if teclas[pygame.K_s]:
                turno.tanque.velocidad_disparo -= 1.5
                if turno.tanque.velocidad_disparo < constantes.LIMITE_VELOCIDAD_MIN:
                    turno.tanque.velocidad_disparo = constantes.LIMITE_VELOCIDAD_MIN
            if teclas[pygame.K_s] and teclas[pygame.K_LSHIFT]:
                turno.tanque.velocidad_disparo -= 3.0
                if turno.tanque.velocidad_disparo < constantes.LIMITE_VELOCIDAD_MIN:
                    turno.tanque.velocidad_disparo = constantes.LIMITE_VELOCIDAD_MIN
            # Verifica disparo del tanque y cambio de turnos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Disparo
                    # Se intancia el disparo
                    disparo = clases.Disparo(
                        turno.tanque.angulo_n, turno.tanque.velocidad_disparo, turno.tanque)
                    if turno.tanque.disparar(pantalla=pantalla, terreno=terreno, ancho=constantes.ANCHO_VENTANA,
                                             alto=constantes.ALTO_VENTANA, disparo=disparo,
                                             altura_terreno=altura_terreno, tanque_enemigo=enemigo):
                        game.ganador = turno
                        terminar_turnos(constantes.JUGADORES)
                    else:
                        cambiar_turnos(jugador_1, jugador_2)

        for mando in mandos:
            if mando.get_button(4):  # LB
                turno.tanque.angulo_n += 0.5
                if turno.tanque.angulo_n > constantes.LIMITE_ANGULO_MAX:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MAX
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            if mando.get_button(4) and mando.get_button(1):  # LB + X
                turno.tanque.angulo_n += 1.5
                if turno.tanque.angulo_n > constantes.LIMITE_ANGULO_MAX:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MAX
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            if mando.get_button(5):  # RB
                turno.tanque.angulo_n -= 0.5
                if turno.tanque.angulo_n < constantes.LIMITE_ANGULO_MIN:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MIN
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            if mando.get_button(5) and mando.get_button(1):  # RB + X
                turno.tanque.angulo_n -= 1.5
                if turno.tanque.angulo_n < constantes.LIMITE_ANGULO_MIN:
                    turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MIN
                turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
            # Verifica si la tecla 'RT' se mantiene presionada
            if mando.get_axis(5) != -1:
                turno.tanque.velocidad_disparo += 1.0
            if mando.get_axis(5) != -1 and mando.get_button(0):
                turno.tanque.velocidad_disparo += 3.0
            # Verifica si la tecla 'LT' se mantiene presionada
            if mando.get_axis(4) != -1:
                turno.tanque.velocidad_disparo -= 1.0
                if turno.tanque.velocidad_disparo < constantes.LIMITE_VELOCIDAD_MIN:
                    turno.tanque.velocidad_disparo = constantes.LIMITE_VELOCIDAD_MIN
            if mando.get_axis(4) != -1 and mando.get_button(0):
                turno.tanque.velocidad_disparo -= 3.0
                if turno.tanque.velocidad_disparo < constantes.LIMITE_VELOCIDAD_MIN:
                    turno.tanque.velocidad_disparo = constantes.LIMITE_VELOCIDAD_MIN
            if mando.get_button(0):
                # Se intancia el disparo
                disparo = clases.Disparo(
                    turno.tanque.angulo_n, turno.tanque.velocidad_disparo, turno.tanque)
                if turno.tanque.disparar(pantalla=pantalla, terreno=terreno, ancho=constantes.ANCHO_VENTANA,
                                         alto=constantes.ALTO_VENTANA, disparo=disparo, altura_terreno=altura_terreno,
                                         tanque_enemigo=enemigo):
                    game.ganador = turno
                    terminar_turnos(constantes.JUGADORES)
                else:
                    cambiar_turnos(jugador_1, jugador_2)

        # VACIA PANTALLA
        fondo.cargar_fondo(pantalla)

        # Mantener el tanque en el terreno
        jugador_1.tanque.posicion_y = constantes.ALTO_VENTANA - \
                                      altura_terreno[jugador_1.tanque.posicion_x]
        jugador_2.tanque.posicion_y = constantes.ALTO_VENTANA - \
                                      altura_terreno[jugador_2.tanque.posicion_x]

        # Terreno
        terreno.dibujar_terreno(
            pantalla=pantalla, ancho=constantes.ANCHO_VENTANA, alto=constantes.ALTO_VENTANA)

        # Se escribe en pantalla la información del pre-disparo de cada jugador
        if jugador_1.puede_jugar:
            UI.info_pre_disparo(pantalla=pantalla, ancho=constantes.ANCHO_VENTANA, alto=constantes.ALTO_VENTANA,
                                texto_jugador="Jugador 1", color_jugador=jugador_1.tanque.color,
                                angulo=jugador_1.tanque.angulo_n, velocidad=jugador_1.tanque.velocidad_disparo)
        elif jugador_2.puede_jugar:
            UI.info_pre_disparo(pantalla=pantalla, ancho=constantes.ANCHO_VENTANA, alto=constantes.ALTO_VENTANA,
                                texto_jugador="Jugador 2", color_jugador=jugador_2.tanque.color,
                                angulo=jugador_2.tanque.angulo_n, velocidad=jugador_2.tanque.velocidad_disparo)
        # Texto con el jugador ganador
        if game.ganador is not None:
            disparo.recorrido(pantalla, turno.tanque.color)
            if game.ganador == jugador_1:
                clases.Escribir.escribir_texto(pantalla=pantalla, texto="Gana el jugador 1", fuente="Arial",
                                               size_fuente=35, color_fuente=(
                        255, 255, 255), color_fondo=jugador_1.tanque.color, x=constantes.ANCHO_VENTANA // 2.5,
                                               y=constantes.ALTO_VENTANA // 2)
            else:
                clases.Escribir.escribir_texto(pantalla=pantalla, texto="Gana el jugador 2", fuente="Arial",
                                               size_fuente=35, color_fuente=(
                        255, 255, 255), color_fondo=jugador_2.tanque.color, x=constantes.ANCHO_VENTANA // 2.5,
                                               y=constantes.ALTO_VENTANA // 2)

            pygame.display.update()

            # Esperar 5 segundos antes de cerrar la ventana
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_espera = 5000
            while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                pass
            running = False
            disparo = None
        else:
            jugador_1.tanque.draw_tank(pantalla)
            jugador_2.tanque.draw_tank(pantalla)
        if disparo is not None:
            disparo.recorrido(pantalla, turno.tanque.color)
            UI.info_post_disparo(pantalla=pantalla, color_jugador=turno.tanque.color, ancho=constantes.ANCHO_VENTANA,
                                 alto=constantes.ALTO_VENTANA, altura=disparo.altura_maxima,
                                 distancia=disparo.distancia_maxima)
            pygame.display.update()
            # Esperar 2 segundos
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_espera = 2000
            while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                pass
            disparo = None

        pygame.display.flip()

        # Limita los FPS a 60
        reloj.tick(60)

    pygame.quit()


main()
