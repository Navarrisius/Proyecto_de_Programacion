import pygame
import math
from Bala import Bala
from Disparo import Disparo
from Escribir import Escribir
from Fondo import Fondo
from Jugador import Jugador
from Partida import Partida
from Tanque import Tanque
from Terreno import Terreno
from UI import UI
from configuraciones import Configuracion
import constantes
import random
import sys
from Boton import Boton


def menu(pantalla, game):
    constantes.PANTALLA = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA), pygame.RESIZABLE, pygame.OPENGL)
    en_menu = True
    reloj = pygame.time.Clock()
    fondo = Fondo()
    png_pessi = pygame.image.load('img/pessi.png')
    png_pessi = pygame.transform.scale(png_pessi, (200, 200))
    png_balon_de_hielo = pygame.image.load('img/balon_de_hielo.png')
    png_balon_de_hielo = pygame.transform.scale(png_balon_de_hielo, (120, 120))
    png_balon_de_hielo = pygame.transform.rotate(png_balon_de_hielo, 12)
    ancho_botón, altura_botón = 0.25, 0.08
    margin_ratio = 0.05  # Margen de separación entre botones

    botones = [
        Boton(0.5 - ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio, ancho_botón,
               altura_botón, "Jugar",
              constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
        Boton(0.5 - ancho_botón / 2, 0.5 + 1.5 * altura_botón, ancho_botón, altura_botón, "Ajustes",
              constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
        Boton(0.5 - ancho_botón / 2, 0.5 + 2.5 * altura_botón + margin_ratio, ancho_botón,
               altura_botón, "Controles",
              constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
        Boton(0.5 - ancho_botón / 2, 0.5 + 3.5 * altura_botón + margin_ratio*2, ancho_botón,
               altura_botón, "Salir", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
    ]
    while en_menu:
        mouse = pygame.mouse.get_pos()
        teclas = pygame.key.get_pressed()
        for event in pygame.event.get():
            if teclas[pygame.K_ESCAPE]:
                en_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                    partida(pantalla, game)
                    en_menu = False
                if botones[1].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                    #tutorial(pantalla, game)
                    configurar_juego(pantalla, game)
                if botones[2].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                    tutorial(pantalla, game)
                if botones[3].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                    sys.exit()
        if not en_menu:
            break
        fondo.cargar_fondo(pantalla,1)
        pantalla.blit(png_pessi, (constantes.ANCHO_VENTANA - 230, constantes.ALTO_VENTANA - 200))
        pantalla.blit(png_balon_de_hielo, (constantes.ANCHO_VENTANA - 110, constantes.ALTO_VENTANA - 120))
        # boton jugar
        Escribir.render_text(pantalla, "PessiTank", (0.593 - ancho_botón / 2, 0.19 + 1.5 * altura_botón), 85,constantes.NEGRO, "timesnewroman")
        Escribir.render_text(pantalla, "PessiTank", (0.597 - ancho_botón / 2, 0.19 + 1.5 * altura_botón), 85, constantes.CELESTE, "timesnewroman")
        ####Escribir.escribir_texto(pantalla, "PessiTank", "timesnewroman", 180, constantes.NEGRO, None,constantes.ANCHO_VENTANA / 2 - 410, constantes.ALTO_VENTANA / 2 - 300)
        ####Escribir.escribir_texto(pantalla, "PessiTank", "timesnewroman", 180, (114,158,188), None,constantes.ANCHO_VENTANA / 2 - 415, constantes.ALTO_VENTANA / 2 - 301)
        png_hielo = pygame.image.load("img/hielo.png").convert_alpha()
        png_hielo = pygame.transform.scale(png_hielo, (320, 220))
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            png_hielo = pygame.transform.scale(png_hielo, (220, 150))
        pantalla.blit(png_hielo, posicion(0.50,0.18,ancho_botón,altura_botón,margin_ratio))

        for boton in botones:
            boton.dibujar(pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)

        pygame.display.flip()
        # Limita los FPS a 60
        reloj.tick(60)


def configurar_juego(pantalla,game):
    font = pygame.font.Font(None, 42)
    change_delay = 100  # Milisegundos de retraso entre cambios
    last_change_time = 0
    ancho_botón, altura_botón = 0.10, 0.04
    margin_ratio = 0.05  # Margen de separación entre botones
    Volver = Boton(0.36 + ancho_botón / 2, 0.65 + 0.5 * altura_botón + margin_ratio, 0.18, 0.10, "Volver", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
    boton_dimenciones = [Boton(0.8 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, "->", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                         Boton(0.5 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, "<-", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)]
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Sal del menú

        keys = pygame.key.get_pressed()

        current_time = pygame.time.get_ticks()

        if current_time - last_change_time > change_delay:
            # Lógica para ajustar las opciones según las teclas presionadas
            if keys[pygame.K_UP]:
                # Aumenta el número de jugadores (limitado a 6)
                constantes.num_jugadores = min(constantes.num_jugadores + 1, 6)
            elif keys[pygame.K_DOWN]:
                # Disminuye el número de jugadores (mínimo 2)
                constantes.num_jugadores = max(constantes.num_jugadores - 1, 2)
            elif keys[pygame.K_RIGHT]:
                # Aumenta el número de partidos
                constantes.num_partidos = min(constantes.num_partidos + 1, 20)
            elif keys[pygame.K_LEFT]:
                # Disminuye el número de partidos (mínimo 1)
                constantes.num_partidos = max(constantes.num_partidos - 1, 1)
            elif keys[pygame.K_e]:
                # Activa/desactiva los efectos del entorno
                constantes.efectos_entorno = not constantes.efectos_entorno

            last_change_time = current_time
        if keys[pygame.K_RETURN]:
            Configuracion(constantes.num_jugadores,800,800,constantes.num_partidos)
        pantalla.fill((208, 237, 250))
        for boton in boton_dimenciones:
            boton.dibujar(pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
        Volver.dibujar(pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
        Escribir.render_text(pantalla, str(constantes.dimenciones),(0.7 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio), 30, constantes.NEGRO,"Arial")
        Escribir.render_text(pantalla, "Ajustes del juego", (0.47 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.NEGRO, "More Sugar")
        # Muestra las opciones y valores en la pantalla
        Escribir.render_text(pantalla, f"Jugadores: {constantes.num_jugadores}", (0.016 + ancho_botón / 2, 0.28 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
        Escribir.render_text(pantalla, "Use las flechas arriba y abajo para aumentar y disminuir los jugadores", (0.38 + ancho_botón / 2, 0.28 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
        Escribir.render_text(pantalla, f"Número de Partidos: {constantes.num_partidos}", (0.05 + ancho_botón / 2, 0.32 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
        Escribir.render_text(pantalla, "Use las flechas derecha e izquierda para aumentar y disminuir jugadores", (0.47 + ancho_botón / 2, 0.32 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
        Escribir.render_text(pantalla, f"Efectos de Entorno: {'Activado' if constantes.efectos_entorno else 'Desactivado'}", (0.08 + ancho_botón / 2, 0.36 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
        Escribir.render_text(pantalla, f"Dimenciones: {constantes.dimenciones[0]},{constantes.dimenciones[1]}", (0.06 + ancho_botón / 2, 0.4 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Volver.si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA = constantes.dimenciones[0], \
                        constantes.dimenciones[1]
                        menu(pantalla, game)       
                if boton_dimenciones[1].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                    constantes.dimenciones[0] = int(constantes.config_defecto.ancho_pantalla)
                    constantes.dimenciones[1] = int(constantes.config_defecto.alto_pantalla)
                if boton_dimenciones[0].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                    constantes.dimenciones[0] = int(constantes.config_maximas.ancho_pantalla)
                    constantes.dimenciones[1] = int(constantes.config_maximas.alto_pantalla)

        pygame.display.update()
        pygame.display.flip()


def posicion(x,y,ancho_botón,altura_botón,margin_ratio):
    pos_x_rel = x + ancho_botón / 2
    pos_y_rel = y - 0.5 * altura_botón + margin_ratio
        # Calcula las coordenadas en función de la resolución actual
    pos_x = constantes.ANCHO_VENTANA * pos_x_rel
    pos_y = constantes.ALTO_VENTANA * pos_y_rel
    return pos_x, pos_y


def tutorial(pantalla, game):
    nuevo_ancho = 100
    nuevo_alto = 100
    if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
        nuevo_alto = 50
        nuevo_ancho = 55
    ancho_botón, altura_botón = 0.10, 0.04
    margin_ratio = 0.05  # Margen de separación entre botones
    Volver = Boton(0.36 + ancho_botón / 2, 0.65 + 0.5 * altura_botón + margin_ratio, 0.18, 0.10, "Volver", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
    while True:
        mouse = pygame.mouse.get_pos()
        pantalla.fill((219, 241, 243))
        Volver.dibujar(pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
        Escribir.render_text(pantalla, "Controles", (0.47 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.NEGRO, "More Sugar")
        png_bala60 = pygame.image.load("img/60mm.png").convert_alpha()
        pantalla.blit(png_bala60, posicion(0.60,0.17,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Bala 60mm", (0.70 + ancho_botón / 2, 0.18 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        Escribir.render_text(pantalla, "Costo $1000", (0.705 + ancho_botón / 2, 0.22 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        Escribir.render_text(pantalla, "Daño 30", (0.688 + ancho_botón / 2, 0.26 - 0.5 * altura_botón + margin_ratio), 25, constantes.NEGRO, "More Sugar")
        png_bala80 = pygame.image.load("img/80mm.png").convert_alpha()
        pantalla.blit(png_bala80, posicion(0.60,0.375,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Bala 80mm", (0.70 + ancho_botón / 2, 0.385 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        Escribir.render_text(pantalla, "Costo $2500", (0.705 + ancho_botón / 2, 0.425 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        Escribir.render_text(pantalla, "Daño 40", (0.688 + ancho_botón / 2, 0.465 - 0.5 * altura_botón + margin_ratio), 25, constantes.NEGRO, "More Sugar")
        png_bala105 = pygame.image.load("img/105mm.png").convert_alpha()
        pantalla.blit(png_bala105, posicion(0.60,0.545,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Bala 105mm", (0.705 + ancho_botón / 2, 0.555 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        Escribir.render_text(pantalla, "Costo $4000", (0.705 + ancho_botón / 2, 0.59 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        Escribir.render_text(pantalla, "Daño 50", (0.688 + ancho_botón / 2, 0.63 - 0.5 * altura_botón + margin_ratio), 25, constantes.NEGRO, "More Sugar")
        
        png_tecla_w = pygame.image.load("img/tecla_w_.png").convert_alpha()
        png_tecla_w_ajustado = pygame.transform.scale(png_tecla_w, (nuevo_ancho, nuevo_alto))
        pantalla.blit(png_tecla_w_ajustado, posicion(-0.017,0.20,ancho_botón,altura_botón,margin_ratio))
        png_tecla_s = pygame.image.load("img/tecla_s_.png").convert_alpha()
        png_tecla_s_ajustado = pygame.transform.scale(png_tecla_s, (nuevo_ancho, nuevo_alto))
        pantalla.blit(png_tecla_s_ajustado,  posicion(-0.017,0.10,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Aumento o disminución de la potencia", (0.3 + ancho_botón / 2, 0.195 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        
        png_tecla_a = pygame.image.load("img/tecla_a_.png").convert_alpha()
        png_tecla_a_ajustado = pygame.transform.scale(png_tecla_a, (nuevo_ancho, nuevo_alto))
        pantalla.blit(png_tecla_a_ajustado,  posicion(-0.04,0.35,ancho_botón,altura_botón,margin_ratio))
        png_tecla_d = pygame.image.load("img/tecla_d_.png").convert_alpha()
        png_tecla_d_ajustado = pygame.transform.scale(png_tecla_d, (nuevo_ancho, nuevo_alto))
        pantalla.blit(png_tecla_d_ajustado,  posicion(0.025,0.35,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Aumento o disminución  del ángulo", (0.28 + ancho_botón / 2, 0.40 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        
        png_tecla_b = pygame.image.load("img/tecla_b.png").convert_alpha()
        png_tecla_b_ajustado = pygame.transform.scale(png_tecla_b, (nuevo_ancho, nuevo_alto))
        pantalla.blit(png_tecla_b_ajustado, posicion(-0.017,0.50,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Cambio de munición", (0.205 + ancho_botón / 2, 0.55 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
        
        png_tecla_espacio = pygame.image.load("img/Space.png").convert_alpha()
        png_tecla_espacio_ajustado = pygame.transform.scale(png_tecla_espacio, (nuevo_ancho, nuevo_alto))
        pantalla.blit(png_tecla_espacio_ajustado, posicion(-0.017,0.65,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Disparar", (0.145 + ancho_botón / 2, 0.69 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")


        png_tecla_shift = pygame.image.load("img/SHIFT.png").convert_alpha()
        png_tecla_shift_ajustado = pygame.transform.scale(png_tecla_shift, (nuevo_ancho, nuevo_alto))
        pantalla.blit(png_tecla_shift_ajustado, posicion(-0.017,0.80,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla, "Aumento o dismunición más rápida ", (0.28 + ancho_botón / 2, 0.85 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Volver.si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA = constantes.dimenciones[0], \
                        constantes.dimenciones[1]
                        menu(pantalla, game)

        pygame.display.update()


def actualizar_info_pantalla():
    info = pygame.display.Info()
    constantes.ANCHO_VENTANA = info.current_w
    constantes.ALTO_VENTANA = info.current_h


def crear_jugadores():
    colores_rgb = {
        "verde_musgo": (47, 69, 56),
        "rojo": (255, 0, 0),
        "azul": (0, 0, 255),
        "rosado": (252, 3, 186),
        "negro": (0, 0, 0),
        "morado" : (99, 11, 87)
    }
    pos_inicial = 0
    pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.num_jugadores
    colores_disponibles = list(colores_rgb.values())
    for i in range(constantes.num_jugadores) :
        color = random.choice(colores_disponibles)
        colores_disponibles.remove(color)
        jugador = Jugador(None, Tanque(color))
        jugador.tanque.posicion_x = random.randint(pos_inicial, pos_final)
        jugador.tanque.posicion_y = 30
        jugador.tanque.angulo_canon = 0
        constantes.JUGADORES.append(jugador)
        pos_inicial = pos_final
        pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.num_jugadores
    elegir_nombres()


def calcular_y(matriz, tanque):
    for y in range(len(matriz)):
        if (matriz[y][tanque.posicion_x] == "x"):
            return y - 1
        

def definir_turnos():
    constantes.ARRAY_TURNOS = constantes.JUGADORES.copy()
    random.shuffle(constantes.ARRAY_TURNOS)
    for jugador in constantes.ARRAY_TURNOS:
        constantes.TANQUES.append(jugador.tanque)


def cambiar_turno():
    constantes.TURNO_ACTUAL += 1
    if constantes.TURNO_ACTUAL >= constantes.num_jugadores:
        constantes.TURNO_ACTUAL = 0


def elegir_nombres():
    nombres = ["Pessi", "Penaldo", "Bendepan", "Empujaland", "Abuelowski", "Fictisius Jr"]
    for jugador in constantes.JUGADORES:
        nombre = random.choice(nombres)
        nombres.remove(nombre)
        jugador.nombre = nombre
    

def terminar_turnos(jugadores):
    posibles_jugadores = []
    for jugador in jugadores:
        jugador.puede_jugar = False
        if jugador.ya_jugado == False:
            posibles_jugadores.append(jugador)
        else:
            jugador.ya_jugado = False
    return posibles_jugadores


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
    constantes.PANTALLA.blit(superficie_texto, rectángulo_texto)


def pausar():
    pausado = True
    pygame.draw.rect(surface=constantes.PANTALLA, color=(208, 237, 250 ),
                        rect=(constantes.ANCHO_VENTANA// 2 - 1200 // 2, constantes.ALTO_VENTANA//2 - 200,
                            1200, 300), border_radius=20)
    mensaje_a_pantalla("Pausado", constantes.BLANCO, -100, tamaño="large")
    mensaje_a_pantalla("Presiona C para continuar jugando o Q para salir", (246, 239, 2 ), 25)
    pygame.display.update()
    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    pausado = False
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        reloj.tick(5)


def terminar_de_juego(ganador, pantalla):
    termino = True
    pygame.draw.rect(surface=pantalla, color=(255, 215, 0, 128),
                         rect=(constantes.ANCHO_VENTANA// 2 - 1400 // 2, constantes.ALTO_VENTANA//2 - 250,
                               1400, 400), border_radius=20)
    mensaje_a_pantalla("Presiona C para reiniciar partida o Q para salir", (34, 113, 179), 25)
    mensaje_a_pantalla(f"Juego terminado. Gana " + ganador.nombre, constantes.BLANCO, -100, tamaño="large")
    pygame.display.flip()
    pygame.display.update()
    while termino:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    termino = False
                    game = Partida()
                    partida(pantalla, game)
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        reloj.tick(5)


def detectar_reinicio(event, pantalla, game):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: 
            clic_x, clic_y = pygame.mouse.get_pos()
            # Verificar si el clic ocurrió dentro de la imagen
            if constantes.ANCHO_VENTANA - 200 <= clic_x <= constantes.ANCHO_VENTANA - 136 and 40 <= clic_y <= 40 + 64:
                limpiar_constantes()
                partida(pantalla, game)

def detectar_termino_partida(event, pantalla, game):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: 
            clic_x, clic_y = pygame.mouse.get_pos()
            # Verificar si el clic ocurrió dentro de la imagen
            if constantes.ANCHO_VENTANA - 100 <= clic_x <= constantes.ANCHO_VENTANA - 30 and 40 <= clic_y <= 37 + 64:
                pygame.mixer.music.load('mp3/aria_math.mp3')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
                limpiar_constantes()
                menu(pantalla, game)

def detectar_musica(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: 
            clic_x, clic_y = pygame.mouse.get_pos()
            # Verificar si el clic ocurrió dentro de la imagen
            if constantes.ANCHO_VENTANA - 300 <= clic_x <= constantes.ANCHO_VENTANA - 230 and 40 <= clic_y <= 37 + 64:
                if constantes.MUSICA_PARTIDA:
                    pygame.mixer.music.set_volume(0)
                    constantes.MUSICA_PARTIDA = False
                else:
                    pygame.mixer.music.set_volume(0.05)
                    constantes.MUSICA_PARTIDA = True

def shoot(turno, tanques, terreno, game):
    # Se intancia el disparo
    disparo = Disparo(turno.tanque.angulo_n, turno.tanque.velocidad_disparo, turno.tanque, Bala(turno.tanque.tipo_bala))
    if turno.tanque.municion[turno.tanque.tipo_bala].unidades > 0:
        tanque_danyado = turno.tanque.disparar(pantalla=constantes.PANTALLA, terreno=terreno, ancho=constantes.ANCHO_VENTANA,
                                    alto=constantes.ALTO_VENTANA, disparo=disparo,
                                    altura_terreno=terreno.matriz, tanques=tanques)
        # Ningun tanque dañado
        if tanque_danyado != -1:
            if tanque_danyado.salud <= 0:
                if turno.tanque == tanque_danyado:
                    detectar_suicidio(turno)
                else:
                    detectar_kill(turno)
                    
            
        terreno.destruir_terreno(constantes.ALTO_VENTANA, constantes.ANCHO_VENTANA, disparo, disparo.proyectil)
            
        turno.tanque.municion[turno.tanque.tipo_bala].unidades -= 1
        turno.tanque.balas -= 1
        cambiar_turno()
        return disparo
    else:
        return None
    

def detectar_suicidio(turno):
    turno.puede_jugar = False
    turno.dinero -= 5000

def detectar_kill(turno):
    turno.kills += 1
    turno.dinero += 5000

def limpiar_constantes():
    constantes.JUGADORES = []
    constantes.TANQUES = []
    constantes.ARRAY_TURNOS = []
    constantes.EN_RONDA_DE_COMPRA = True
    constantes.RONDA_ACTUAL = 1


def controles(event, teclas, turno, tanques, terreno, game):
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
    # Cambio de tipo de municion al apretar la tecla 'Q' estas rotan en un ciclo
    if teclas[pygame.K_q]:
        if turno.tanque.tipo_bala < 2:
            turno.tanque.tipo_bala += 1
        else:
            turno.tanque.tipo_bala = 0

    # Verifica disparo del tanque y cambio de turnos
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:  # Disparo
            constantes.DISPARO = shoot(turno, tanques, terreno, game)


def ui_pre_disparo(ui, pantalla, turno):
    ui.rectangulo(pantalla)
    ui.texto_ajustes_disparo(pantalla)
    ui.texto_angulo(pantalla, turno.tanque.angulo_n)
    ui.texto_velocidad(pantalla, turno.tanque.velocidad_disparo)
    ui.texto_dinero(pantalla, turno.dinero)
    ui.texto_salud(pantalla, turno.tanque.salud)
    ui.texto_tipo_bala(pantalla, turno.tanque.tipo_bala)
    ui.cantidad_img_balas(pantalla, turno.tanque.tipo_bala, turno.tanque.municion[turno.tanque.tipo_bala].unidades)
    ui.ronda_actual(pantalla)
    ui.kills(pantalla, turno.kills)


def iniciar_tanques(terreno):
    for jugador in constantes.JUGADORES :
        jugador.tanque.posicion_y = calcular_y(terreno.matriz, jugador.tanque)
        jugador.tanque.caida_tanque = jugador.tanque.posicion_y


def controles_compra(teclas, turno):
    # Cambio de tipo de municion al apretar la tecla 'Q' estas rotan en un ciclo
    if teclas[pygame.K_q]:
        if turno.tanque.tipo_bala < 2:
            turno.tanque.tipo_bala += 1
        else:
            turno.tanque.tipo_bala = 0

    # Comprar al apretar la tecla 'B'
    if teclas[pygame.K_b]:
        sound = pygame.mixer.Sound('mp3/sonido_compra.mp3')
        sound.set_volume(0.2)
        if turno.tanque.tipo_bala == 0 and turno.dinero >= 1000:
            turno.comprar_bala_60mm()
            sound.play()
        if turno.tanque.tipo_bala == 1 and turno.dinero >= 2500:
            turno.comprar_bala_80mm()
            sound.play()
        if turno.tanque.tipo_bala == 2 and turno.dinero >= 4000:
            turno.comprar_bala_105mm()
            sound.play()

    # Vender al apretar la tecla 'S'
    if teclas[pygame.K_s]:
        sound = pygame.mixer.Sound('mp3/sonido_venta.mp3')
        sound.set_volume(0.2)
        if turno.tanque.tipo_bala == 0 and turno.tanque.municion[0].unidades > 0:
            turno.vender_bala_60mm()
            sound.play()
        if turno.tanque.tipo_bala == 1 and turno.tanque.municion[1].unidades > 0:
            turno.vender_bala_80mm()
            sound.play()
        if turno.tanque.tipo_bala == 2 and turno.tanque.municion[2].unidades > 0:
            turno.vender_bala_105mm()
            sound.play()
    
    if teclas[pygame.K_n]:
        constantes.TURNO_ACTUAL += 1


def combrobar_compra_de_todos_los_jugadores():
    if constantes.TURNO_ACTUAL >= constantes.CANT_JUGADORES:
        constantes.EN_RONDA_DE_COMPRA = False
        constantes.TURNO_ACTUAL = 0

def cambiar_musica(nueva_cancion):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(nueva_cancion)
    pygame.mixer.music.play()


def tanque_sin_municion(tanque_turno):
    if tanque_turno.municion[0].unidades == 0 and tanque_turno.municion[1].unidades == 0 and tanque_turno.municion[2].unidades == 0:
        return True
    else:
        return False
    

def combrobar_municion_tanques():
    tanques_sin_municion = 0
    for tanque in constantes.TANQUES:
        if tanque_sin_municion(tanque):
            tanques_sin_municion += 1

    if tanques_sin_municion == len(constantes.TANQUES) and constantes.EN_RONDA_DE_COMPRA == False:
        avanzar_partido()


def avanzar_partido():
    constantes.RONDA_ACTUAL += 1
    constantes.EN_RONDA_DE_COMPRA = True
    for jugador in constantes.JUGADORES:
        jugador.dinero += 10000
        jugador.tanque.salud = 100

    pos_inicial = 0
    pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.num_jugadores
    for jugador in constantes.JUGADORES:
        jugador.tanque.posicion_x = random.randint(pos_inicial, pos_final)
        jugador.tanque.posicion_y = 30
        jugador.tanque.angulo_canon = 0
        pos_inicial = pos_final
        pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.num_jugadores

    altura_terreno = constantes.TERRENO.generar_terreno_perlin()
    constantes.TERRENO.generar_matriz(constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA, altura_terreno)
    iniciar_tanques(constantes.TERRENO)
    definir_turnos()
    
        


def saltar_turno_tanque_sin_municion(turno):
    if tanque_sin_municion(turno.tanque):
        cambiar_turno()


def queda_un_jugador_vivo():
    jugadores_vivos = 0
    for tanque in constantes.TANQUES:
        if tanque.salud > 0:
            jugadores_vivos += 1
    if jugadores_vivos == 1:
        return True
    else:
        return False


def comprobar_jugadores_vivos():
    if queda_un_jugador_vivo() and constantes.EN_RONDA_DE_COMPRA == False:
        avanzar_partido()


def partida(pantalla, game):
    global reloj
    pygame.mixer.init()
    pygame.mixer.music.load('mp3/C418_Living_Mice.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    constantes.JUGADORES = []
    constantes.MUSICA = 'mp3/C418_Living_Mice.mp3'
    crear_jugadores()
    turno = None
    constantes.TERRENO = Terreno()
    fondo = Fondo()
    running = game.en_partida
    pygame.time.Clock()
    ui = UI()
    img_reiniciar = pygame.image.load("img/reiniciar.png")
    img_reiniciar = pygame.transform.scale(img_reiniciar, (64, 64))
    img_terminar_partida = pygame.image.load("img/terminar_partida.png")
    img_terminar_partida = pygame.transform.scale(img_terminar_partida, (70, 70))
    img_musica = pygame.image.load("img/musica.png")
    img_musica = pygame.transform.scale(img_musica, (70, 70))
    img_linea_diagonal_sin_musica = pygame.image.load("img/linea_diagonal.png")
    altura_terreno = constantes.TERRENO.generar_terreno_perlin()
    constantes.TERRENO.generar_matriz(constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA, altura_terreno)
    iniciar_tanques(constantes.TERRENO)
    definir_turnos()

    while running:
        turno = constantes.ARRAY_TURNOS[constantes.TURNO_ACTUAL]
        reloj = pygame.time.Clock()
        teclas = pygame.key.get_pressed()
        if constantes.EN_RONDA_DE_COMPRA:
            if constantes.MUSICA != 'mp3/C418_Living_Mice.mp3':
                cambiar_musica('mp3/C418_Living_Mice.mp3')
                constantes.MUSICA = 'mp3/C418_Living_Mice.mp3'
            for event in pygame.event.get():
                detectar_reinicio(event, pantalla, game)
                detectar_termino_partida(event, pantalla, game)
                detectar_musica(event)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    NUEVO_ANCHO, NUEVA_ALTURA = event.size
                    pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE, pygame.OPENGL)
                    constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA = NUEVO_ANCHO, NUEVA_ALTURA
                elif teclas[pygame.K_ESCAPE]:
                    pausar()
                controles_compra(teclas, turno)
                combrobar_compra_de_todos_los_jugadores()
        else:
            for event in pygame.event.get():
                saltar_turno_tanque_sin_municion(turno)
                if constantes.MUSICA != 'mp3/Death_by_Glamour.mp3':
                    cambiar_musica('mp3/Death_by_Glamour.mp3')
                    constantes.MUSICA = 'mp3/Death_by_Glamour.mp3'
                detectar_reinicio(event, pantalla, game)
                detectar_termino_partida(event, pantalla, game)
                detectar_musica(event)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    NUEVO_ANCHO, NUEVA_ALTURA = event.size
                    pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE, pygame.OPENGL)
                    constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA = NUEVO_ANCHO, NUEVA_ALTURA
                elif teclas[pygame.K_ESCAPE]:
                    pausar()
                controles(event, teclas, turno, constantes.TANQUES, constantes.TERRENO, game)

        # VACIA PANTALLA
        fondo.cargar_fondo(pantalla, 1)

        # Mantener el tanque en el terreno y comprobar caida
        for jugador in constantes.JUGADORES:
            jugador.tanque.posicion_y = calcular_y(constantes.TERRENO.matriz, jugador.tanque)
            if jugador.tanque.posicion_y != jugador.tanque.caida_tanque:
                jugador.tanque.calcular_damage_caida(jugador.tanque.caida_tanque)
                ui.mensaje_caida(pantalla=pantalla, ancho=constantes.ANCHO_VENTANA, diff_y=abs(jugador.tanque.posicion_y - jugador.tanque.caida_tanque))
                jugador.tanque.caida_tanque = jugador.tanque.posicion_y

        for jugador in constantes.JUGADORES :
            if jugador.tanque.salud <= 0 :
                jugador.tanque.corregir_salud()
                jugador.vivo = False

        # Terreno
        constantes.TERRENO.dibujar_terreno(pantalla)
        ui.barras_de_salud(pantalla)
        

        ui_pre_disparo(ui, pantalla, turno)

        ui.texto_jugador(pantalla, turno.tanque.color, turno.nombre)

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
            pygame.display.update()
            
        else:
            # Botón reinicio
            pantalla.blit(img_reiniciar, (constantes.ANCHO_VENTANA - 200, 40))

            # Botón término partida
            pantalla.blit(img_terminar_partida, (constantes.ANCHO_VENTANA - 100, 37))

            # Botón música
            if constantes.MUSICA_PARTIDA:
                pantalla.blit(img_musica, (constantes.ANCHO_VENTANA - 300, 37))
            else:
                pantalla.blit(img_musica, (constantes.ANCHO_VENTANA - 300, 37))
                pantalla.blit(img_linea_diagonal_sin_musica, (constantes.ANCHO_VENTANA - 297, 40))

            for jugador in constantes.JUGADORES :
                jugador.tanque.draw_tank(pantalla)

        if constantes.DISPARO is not None:
            disparo = constantes.DISPARO
            disparo.recorrido(pantalla, turno.tanque.color)
            ui.info_bala(pantalla, -1, int(disparo.altura_maxima), int(disparo.distancia_maxima))
            pygame.display.update()
            # Esperar 2 segundos
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_espera = 2000
            while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                pass
            constantes.DISPARO = None
        
        if constantes.EN_RONDA_DE_COMPRA:
            ui.ronda_compra(pantalla, constantes.ANCHO_VENTANA)
        
        combrobar_municion_tanques()
        comprobar_jugadores_vivos()

        pygame.display.flip()

        # Limita los FPS a 60
        reloj.tick(60)