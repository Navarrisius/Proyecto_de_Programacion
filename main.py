import pygame
import math
import clases
import constantes
import random
import sys

def menu(pantalla, mandos, game):
    en_menu = True
    reloj = pygame.time.Clock()
    fondo = clases.Fondo()
    while en_menu:
        mouse = pygame.mouse.get_pos()
        teclas = pygame.key.get_pressed()
        for event in pygame.event.get():
            if teclas[pygame.K_ESCAPE]:
                en_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((constantes.ANCHO_VENTANA / 2 - 235 <= mouse[0] <= constantes.ANCHO_VENTANA / 2 - 235 + 470) and
                        (constantes.ALTO_VENTANA / 2 - 60 <= mouse[1] <= constantes.ALTO_VENTANA / 2 - 60 + 120)):
                    partida(pantalla, mandos, game)
                    en_menu = False
                if ((mouse[0] >= constantes.ANCHO_VENTANA / 2 - 235 and mouse[
                    0] <= constantes.ANCHO_VENTANA / 2 - 235 + 470) and (
                        mouse[1] >= constantes.ALTO_VENTANA / 2 + 90 and mouse[
                    1] <= constantes.ALTO_VENTANA / 2 + 60 + 120)):
                    pass
                if (mouse[0] >= constantes.ANCHO_VENTANA / 2 - 235 and mouse[
                    0] <= constantes.ANCHO_VENTANA / 2 - 235 + 470) and (
                        mouse[1] >= constantes.ALTO_VENTANA / 2 + 245 and mouse[
                    1] <= constantes.ALTO_VENTANA / 2 + 245 + 120):
                    en_menu = False
        if not en_menu:
            break
        fondo.cargar_fondo(pantalla)
        # boton jugar
        clases.Escribir.escribir_texto(pantalla, "PessiTank", "timesnewroman", 180, constantes.NEGRO, None,
                                       constantes.ANCHO_VENTANA / 2 - 410, constantes.ALTO_VENTANA / 2 - 300)
        clases.Escribir.escribir_texto(pantalla, "PessiTank", "timesnewroman", 180, (114,158,188), None,
                                       constantes.ANCHO_VENTANA / 2 - 415, constantes.ALTO_VENTANA / 2 - 301)
        png_hielo = pygame.image.load("img/hielo.png").convert_alpha()
        png_hielo = pygame.transform.scale(png_hielo, (320, 220))
        pantalla.blit(png_hielo, (constantes.ANCHO_VENTANA / 2 + 235, constantes.ALTO_VENTANA / 2 - 300))

        pygame.draw.rect(pantalla, constantes.BLANCO,
                         (constantes.ANCHO_VENTANA / 2 - 235, constantes.ALTO_VENTANA / 2 - 60, 470, 120), 60, 50)
        clases.Escribir.escribir_texto(pantalla, "Jugar", "More Sugar", 150, constantes.NEGRO, None,
                                       constantes.ANCHO_VENTANA / 2 - 150, constantes.ALTO_VENTANA / 2 - 55)
        # boton configuracion
        pygame.draw.rect(pantalla, constantes.BLANCO,
                         (constantes.ANCHO_VENTANA / 2 - 235, constantes.ALTO_VENTANA / 2 + 90, 470, 120), 60, 50)
        clases.Escribir.escribir_texto(pantalla, "Controles", "More Sugar", 130, constantes.NEGRO, None,
                                       constantes.ANCHO_VENTANA / 2 - 210, constantes.ALTO_VENTANA / 2 + 100)
        # boton salir
        pygame.draw.rect(pantalla, constantes.BLANCO,
                         (constantes.ANCHO_VENTANA / 2 - 235, constantes.ALTO_VENTANA / 2 + 245, 470, 120), 60, 50)
        clases.Escribir.escribir_texto(pantalla, "Salir", "More Sugar", 150, constantes.NEGRO, None,
                                       constantes.ANCHO_VENTANA / 2 - 125, constantes.ALTO_VENTANA / 2 + 255)
        if ((constantes.ANCHO_VENTANA / 2 - 235 <= mouse[0] <= constantes.ANCHO_VENTANA / 2 - 235 + 470) and
                (constantes.ALTO_VENTANA / 2 - 60 <= mouse[1] <= constantes.ALTO_VENTANA / 2 - 60 + 120)):
            pygame.draw.rect(pantalla, (114,158,188),
                            (constantes.ANCHO_VENTANA / 2 - 235, constantes.ALTO_VENTANA / 2 - 60, 470, 120), 60, 50)
            clases.Escribir.escribir_texto(pantalla, "Jugar", "More Sugar", 150, constantes.BLANCO, None,
                                        constantes.ANCHO_VENTANA / 2 - 150, constantes.ALTO_VENTANA / 2 - 55)
        if ((mouse[0] >= constantes.ANCHO_VENTANA / 2 - 235 and mouse[
            0] <= constantes.ANCHO_VENTANA / 2 - 235 + 470) and (
                mouse[1] >= constantes.ALTO_VENTANA / 2 + 90 and mouse[
            1] <= constantes.ALTO_VENTANA / 2 + 60 + 120)):
                    pygame.draw.rect(pantalla, (114,158,188),
                         (constantes.ANCHO_VENTANA / 2 - 235, constantes.ALTO_VENTANA / 2 + 90, 470, 120), 60, 50)
                    clases.Escribir.escribir_texto(pantalla, "Controles", "More Sugar", 130, constantes.BLANCO, None,
                                                constantes.ANCHO_VENTANA / 2 - 210, constantes.ALTO_VENTANA / 2 + 100)
        if (mouse[0] >= constantes.ANCHO_VENTANA / 2 - 235 and mouse[
            0] <= constantes.ANCHO_VENTANA / 2 - 235 + 470) and (
                mouse[1] >= constantes.ALTO_VENTANA / 2 + 245 and mouse[
            1] <= constantes.ALTO_VENTANA / 2 + 245 + 120):
            pygame.draw.rect(pantalla, (114,158,188),
                            (constantes.ANCHO_VENTANA / 2 - 235, constantes.ALTO_VENTANA / 2 + 245, 470, 120), 60, 50)
            clases.Escribir.escribir_texto(pantalla, "Salir", "More Sugar", 150, constantes.BLANCO, None,
                                        constantes.ANCHO_VENTANA / 2 - 125, constantes.ALTO_VENTANA / 2 + 255)
        pygame.display.flip()
        # Limita los FPS a 60
        reloj.tick(60)


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
    jugador_1.tanque.posicion_x = random.randint(30, constantes.ANCHO_VENTANA // 2 - 200)
    jugador_1.tanque.posicion_y = 30
    jugador_1.tanque.angulo_n = 0
    jugador_1.tanque.angulo_canon = (math.radians(jugador_1.tanque.angulo_n))

    # Se crea el jugador 2
    jugador_2 = clases.Jugador(None, clases.Tanque(segundo_color))
    jugador_2.tanque.posicion_x = random.randint(constantes.ANCHO_VENTANA // 2 + 200, constantes.ANCHO_VENTANA - 60)
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


def calcular_y(matriz, tanque):
    for y in range(len(matriz)):
        if (matriz[y][tanque.posicion_x] == "x"):
            return y - 1


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


def barras_de_salud(tanque, pantalla):
    if tanque.salud > 75:
        color_de_salud_del_jugador = (0, 143, 57)
    elif tanque.salud > 50:
        color_de_salud_del_jugador = (255, 255, 0)
    else:
        color_de_salud_del_jugador = (255, 0, 0)

    pygame.draw.rect(pantalla, (0, 0, 0), (tanque.posicion_x - 55, tanque.posicion_y + 17, 102, 27))
    pygame.draw.rect(pantalla, color_de_salud_del_jugador, (tanque.posicion_x - 57, tanque.posicion_y + 15, tanque.salud, 25))


def objetos_de_texto(text, color, size="small"):
    # Diccionario de fuentes y tamaños
    fuentes = {
        "small": pygame.font.SysFont("comicsansms", 25),
        "medium": pygame.font.SysFont("comicsansms", 50),
        "large": pygame.font.SysFont("Yu Mincho Demibold", 100),
        "vsmall": pygame.font.SysFont("Yu Mincho Demibold", 25)
    }
    if size in fuentes:
        textSurface = fuentes[size].render(text, True, color)
        return textSurface, textSurface.get_rect()
    else:
        raise ValueError("Tamaño de fuente no válido: " + size)


def mensaje_a_pantalla(msg, color, y_desplazamiento=0, tamaño="medium"):
    superficie_texto, rectángulo_texto = objetos_de_texto(msg, color, tamaño)
    rectángulo_texto.center = (int(constantes.ANCHO_VENTANA / 2), int(constantes.ALTO_VENTANA / 2) + y_desplazamiento)
    pantalla.blit(superficie_texto, rectángulo_texto)


def pausar():
    pausado = True
    pygame.draw.rect(surface=pantalla, color=(208, 237, 250 ),
                        rect=(constantes.ANCHO_VENTANA// 2 - 1200 // 2, constantes.ALTO_VENTANA//2 - 200,
                            1200, 300), border_radius=20)
    mensaje_a_pantalla("Pausado", constantes.BLANCO, -100, tamaño="large")
    mensaje_a_pantalla("Presiona C para continuar jugando o Q para salir", (246, 239, 2 ), 25)
    pygame.display.update()
    while pausado:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    pausado = False
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    quit()()

        reloj.tick(5)


def terminar_de_juego(ganador, pantalla):
    termino = True
    pygame.draw.rect(surface=pantalla, color=(255, 215, 0, 128),
                         rect=(constantes.ANCHO_VENTANA// 2 - 1400 // 2, constantes.ALTO_VENTANA//2 - 250,
                               1400, 400), border_radius=20)
    mensaje_a_pantalla("Presiona C para reiniciar partida o Q para salir", (34, 113, 179), 25)
    if ganador == jugador_1:
        mensaje_a_pantalla(f"Juego terminado. Gana Jugador 1", constantes.BLANCO, -100, tamaño="large")
    else:
        mensaje_a_pantalla(f"Juego terminado. Gana Jugador 2", constantes.BLANCO, -100, tamaño="large")
    pygame.display.flip()
    pygame.display.update()
    while termino:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    termino = False
                    mandos = []
                    game = clases.Partida()
                    partida(pantalla, mandos, game)
                elif evento.key == pygame.K_q:
                    pygame.quit()

        reloj.tick(5)


def partida(pantalla, mandos, game):
    global reloj , jugador_1, jugador_2
    crear_jugadores()
    jugador_1 = constantes.JUGADORES[0]
    jugador_2 = constantes.JUGADORES[1]
    terreno = clases.Terreno()
    fondo = clases.Fondo()
    running = game.en_partida
    pygame.time.Clock()
    disparo = None
    altura_terreno = [0] * constantes.ANCHO_VENTANA
    UI = clases.UI()

    for x in range(constantes.ANCHO_VENTANA):
        altura_terreno[x] += terreno.generar_terreno(x, 250, constantes.ALTO_VENTANA - 100)

    terreno.generar_matriz(constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA, altura_terreno)

    while running:
        reloj = pygame.time.Clock()
        teclas = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
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
                pausar()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                terreno.destruir_terreno(mouse[0], mouse[1], constantes.ALTO_VENTANA, constantes.ANCHO_VENTANA, 40)
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
            # Cambio de tipo de municion al apretar la tecla 'B' estas rotan en un ciclo
            if teclas[pygame.K_b]:
                if turno.tanque.tipo_bala < 2:
                    turno.tanque.tipo_bala += 1
                else:
                    turno.tanque.tipo_bala = 0
            # Verifica disparo del tanque y cambio de turnos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Disparo
                    # Se intancia el disparo
                    disparo = clases.Disparo(turno.tanque.angulo_n, turno.tanque.velocidad_disparo, turno.tanque,
                                             clases.Bala(turno.tanque.tipo_bala))
                    if turno.tanque.municion[turno.tanque.tipo_bala].unidades > 0:
                        if turno.tanque.disparar(pantalla=pantalla, terreno=terreno, ancho=constantes.ANCHO_VENTANA,
                                                 alto=constantes.ALTO_VENTANA, disparo=disparo,
                                                 altura_terreno=terreno.matriz, tanque_enemigo=enemigo):
                            print("impacto enemigo")
                            enemigo.salud -= disparo.proyectil.dano
                            if enemigo.salud <= 0:
                                game.ganador = turno
                                terminar_turnos(constantes.JUGADORES)
                            else:
                                cambiar_turnos(jugador_1, jugador_2)
                        else:
                            terreno.destruir_terreno(int(disparo.x_bala), int(disparo.y_bala), constantes.ALTO_VENTANA,
                                                     constantes.ANCHO_VENTANA, turno.tanque.municion[turno.tanque.tipo_bala].radio_impacto)
                            cambiar_turnos(jugador_1, jugador_2)
                        turno.tanque.municion[turno.tanque.tipo_bala].unidades -= 1
                    else:
                        print("No hay municion")

        # VACIA PANTALLA
        fondo.cargar_fondo(pantalla)

        # Mantener el tanque en el terreno
        jugador_1.tanque.posicion_y = calcular_y(terreno.matriz, jugador_1.tanque)
        jugador_2.tanque.posicion_y = calcular_y(terreno.matriz, jugador_2.tanque)

        # Terreno
        terreno.dibujar_terreno(pantalla)
        barras_de_salud(jugador_1.tanque, pantalla)
        barras_de_salud(jugador_2.tanque, pantalla)
        # Se escribe en pantalla la información del pre-disparo de cada jugador
        if jugador_1.puede_jugar:
            UI.info_pre_disparo(pantalla=pantalla, ancho=constantes.ANCHO_VENTANA, alto=constantes.ALTO_VENTANA,
                                texto_jugador="Turno del Jugador 1", color_jugador=jugador_1.tanque.color,
                                angulo=jugador_1.tanque.angulo_n, velocidad=jugador_1.tanque.velocidad_disparo, tanque_jugador= jugador_1.tanque)
        elif jugador_2.puede_jugar:
            UI.info_pre_disparo(pantalla=pantalla, ancho=constantes.ANCHO_VENTANA, alto=constantes.ALTO_VENTANA,
                                texto_jugador="Turno del Jugador 2", color_jugador=jugador_2.tanque.color,
                                angulo=jugador_2.tanque.angulo_n, velocidad=jugador_2.tanque.velocidad_disparo, tanque_jugador= jugador_2.tanque)
        # Texto con el jugador ganador
        if game.ganador is not None:

            pygame.mixer.music.stop()
            
            disparo.recorrido(pantalla, turno.tanque.color)
            # Esperar 5 segundos antes de cerrar la ventana
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_espera = 5000
            while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                pygame.display.update()
                terminar_de_juego(game.ganador, pantalla)
                # pass
            pygame.display.update()
            
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


def main():
    global pantalla
    # Se inicia Pygame y variables importantes dentro de la ejecución
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('mp3/aria_math.mp3')
    pygame.mixer.music.set_volume(0.02)
    pygame.mixer.music.play(-1)
    img_ventana = pygame.image.load('img/pessi.png')
    pygame.display.set_icon(img_ventana)
    pygame.display.set_caption(constantes.NOMBRE_VENTANA)
    actualizar_info_pantalla()
    pantalla = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA), pygame.RESIZABLE,
                                       pygame.OPENGL)
    game = clases.Partida()
    # Joystick
    pygame.joystick.init()
    mandos = []
    menu(pantalla, mandos, game)
    pygame.quit()


main()