import pygame
import math
import random

import constantes


class Bala:
    tipo_bala = None
    dano = None
    radio_bala = None
    unidades = None
    radio_impacto = None

    def __init__(self, tipo):
        if tipo == 0:
            self.radio_bala = 6
            self.dano = 30
            self.unidades = 3
            self.radio_impacto = 12
        elif tipo == 1:
            self.radio_bala = 8
            self.dano = 40
            self.unidades = 10
            self.radio_impacto = 23
        elif tipo == 2:
            self.radio_bala = 10
            self.dano = 50
            self.unidades = 3
            self.radio_impacto = 40

class Disparo:
    proyectil = None
    angulo_grados = None
    angulo_radianes = 0
    velocidad_inicial = None
    velocidad_actual = 0
    altura_maxima = 0
    distancia_maxima = 0
    x_bala = None
    y_bala = None
    x_inicial = None
    velocidad_x = None
    velocidad_y = None
    tiempo = 0.1
    impacto_terreno = None
    impacto_tanque = None
    autor = None
    eje_x = []
    eje_y = []

    def __init__(self, angulo_grados, velocidad_inicial, autor, bala):
        self.proyectil = bala
        self.angulo_grados = angulo_grados
        self.velocidad_inicial = velocidad_inicial
        self.angulo_radianes = math.radians(angulo_grados)
        self.velocidad_x = velocidad_inicial * math.cos(self.angulo_radianes)
        self.velocidad_y = -velocidad_inicial * math.sin(self.angulo_radianes)
        self.autor = autor
        self.eje_x = []
        self.eje_y = []

    def actualizar(self):
        self.x_bala += self.velocidad_x * self.tiempo
        self.y_bala += (self.velocidad_y * self.tiempo) + (0.5 * 9.81 * (self.tiempo ** 2))
        self.velocidad_y += 9.81 * self.tiempo
        self.eje_x.append(self.x_bala)
        self.eje_y.append(self.y_bala)
        self.velocidad_actual = math.sqrt(self.velocidad_x ** 2 + self.velocidad_y ** 2)

    def dibujar(self, pantalla, ancho, alto, color):
        pygame.draw.circle(pantalla, color, (int(self.x_bala), int(self.y_bala)), self.proyectil.radio_bala)

    def calcular_altura_maxima(self):
        self.altura_maxima = abs((self.velocidad_inicial ** 2 * (math.sin(self.angulo_radianes) ** 2)) / (2 * 9.81))

    def calcular_distancia_maxima(self, tanque_posicion_x):
        self.distancia_maxima = abs(self.x_bala - self.distancia_maxima - tanque_posicion_x)

    def verificar_impacto_tanque_enemigo(self, tanque_enemigo):
        if (self.y_bala >= tanque_enemigo.posicion_y - 23) and (
                tanque_enemigo.posicion_x - 35<= self.x_bala <= tanque_enemigo.posicion_x + 35):
            return 1
        else:
            return 0

    def recorrido(self, pantalla, color):
        for i in range(len(self.eje_x)):
            pygame.draw.circle(pantalla, color, (int(self.eje_x[i]), int(self.eje_y[i])), 2)


class Jugador:
    nombre = None
    tanque = None
    puede_jugar = False

    def __init__(self, nombre, tanque):
        self.nombre = nombre
        self.tanque = tanque


class Partida:
    en_partida = None
    ganador = None
    def __init__(self):
        self.en_partida = True


class Terreno:
    def __init__(self):
        self.constante_oscilacion = random.uniform(0.01, 0.0135)
        self.matriz = []
        self.arreglo = []
        self.tipo = random.randint(1,3)

    def generar_terreno_perlin(self):
        gradientes = [random.uniform(-1, 1) for _ in range(256)]
        #Funcion para la atenuacion
        def fade(t):
            return (t**3) * (t * (t * 6 - 15) + 10)
        #Funcion basica para ruido de perlin
        def perlin(x):
            X = int(x) & 255
            x -= int(x)
            u = fade(x)
            a = gradientes[X]
            b = gradientes[X + 1]
            val1 = a * x
            val2 = b * (x - 1)
            return (1 - u) * val1 + u * val2
        arr = []
        for x in range(constantes.ANCHO_VENTANA):
            arr.append(int(constantes.ALTO_VENTANA / 2 + perlin(x * 0.006) * 600))
        return arr

    def dibujar_terreno(self, pantalla):
        for pos in range(len(self.arreglo)):
            if pos % 2 == 0:
                pygame.draw.line(pantalla, (173, 204, 246), self.arreglo[pos], self.arreglo[pos + 1])

    def generar_matriz(self, ancho_ventana, alto_ventana, arreglo_terreno):
            self.matriz = [['x' if x >= arreglo_terreno[y] else 'o' for y in range(ancho_ventana)] for x in range(alto_ventana)]
            self.generar_arreglo_m()

    def destruir_terreno(self, centro_x, centro_y, alto, ancho, radio):
        for y in range(max(0, centro_y - radio), min(alto, centro_y + radio)):
            for x in range(max(0, centro_x - radio), min(ancho, centro_x + radio)):
                distancia = ((x - centro_x) ** 2 + (y - centro_y) ** 2) ** 0.5
                if distancia <= radio:
                    self.matriz[y][x] = "o"
        self.generar_arreglo_m()


    def generar_arreglo_m(self):
        self.arreglo = []
        for y in range(len(self.matriz[0])):
            x = 0
            while x < len(self.matriz):
                if self.matriz[x][y] == 'x':
                    pos_inicial = (y, x)
                    while x < len(self.matriz) and self.matriz[x][y] == 'x':
                        x += 1
                    pos_final = (y, x - 1)
                    self.arreglo.extend((pos_inicial, pos_final))
                x += 1

    def mover_o_hacia_abajo(self):
        for x in range(len(self.matriz[0])):
            for y in range(len(self.matriz) - 1):
                if self.matriz[y][x] == 'o' and self.matriz[y + 1][x] == 'x':
                    # Intercambiar 'o' y 'x'
                    self.matriz[y][x], self.matriz[y + 1][x] = self.matriz[y + 1][x], self.matriz[y][x]


class Fondo:
    mountain_png = None
    fondo_terreno = None

    def __init__(self):
        self.mountain_png = pygame.image.load("img/mountain.png").convert_alpha()

    def cargar_fondo(self, screen, tipo):
        if tipo == 1:
            screen.blit(self.mountain_png, (0, 0))


class Tanque:
    municion = None
    tipo_bala = None
    salud = 100
    color = None
    posicion_x = None
    posicion_y = None
    angulo_n = None
    angulo_canon = None
    velocidad_disparo = 50
    turret_end = None
    imagen = None
    
    def __init__(self, color):
        self.municion = [Bala(0), Bala(1), Bala(2)]
        self.color = color
        self.tipo_bala = 0
        if color == (99, 11, 87):
            self.imagen = pygame.image.load("img/tanque_morado.png").convert_alpha()
        elif color == (0, 0, 255):
            self.imagen = pygame.image.load("img/tanque_azul.png").convert_alpha()
        elif color == (255, 0, 0):
            self.imagen = pygame.image.load("img/tanque_rojo.png").convert_alpha()
        elif color == (47, 69, 56):
            self.imagen = pygame.image.load("img/tanque_verde_musgo.png").convert_alpha()
        elif color == (0, 0, 0):
            self.imagen = pygame.image.load("img/tanque_negro.png").convert_alpha()

    def draw_tank(self, pantalla):
        turret_length = 30
        turret_start = (self.posicion_x - 5, self.posicion_y - 25)
        self.turret_end = (self.posicion_x - 5 + turret_length * math.cos(self.angulo_canon),
                           self.posicion_y - 25 - turret_length * math.sin(self.angulo_canon))
        pygame.draw.line(pantalla, "gray", turret_start, self.turret_end, 4)

        pantalla.blit(self.imagen, (self.posicion_x - 40, self.posicion_y - 40))

    def disparar(self, pantalla, ancho, alto, terreno, disparo, altura_terreno, tanque_enemigo):
        disparo.x_bala = self.turret_end[0]
        disparo.y_bala = self.turret_end[1]
        disparo.x_inicial = self.turret_end[0]
        disparo.calcular_altura_maxima()
        fondo = Fondo()
        while True:
            fondo.cargar_fondo(pantalla, 1)

            # Si la bala sale de los limites laterales de la pantalla
            if disparo.x_bala >= ancho:
                disparo.distancia_maxima = -1
                return 0
            if disparo.x_bala <= 0:
                disparo.distancia_maxima = -1
                return 0

            disparo.actualizar()
            disparo.dibujar(pantalla, ancho, alto, self.color)
            try:
                # IMPACTO CON TERRENO
                if disparo.y_bala > 0 and altura_terreno[int(disparo.y_bala)][int(disparo.x_bala)] == "x":
                    disparo.impacto_terreno = True
                    disparo.calcular_distancia_maxima(self.posicion_x)
                    return 0
            # BALA FUERA DEL MAPA
            except IndexError:
                None
            # IMPACTO CON TANQUE ENEMIGO
            if disparo.verificar_impacto_tanque_enemigo(tanque_enemigo):
                disparo.impacto_tanque = True
                disparo.calcular_distancia_maxima(self.posicion_x)
                return 1
            terreno.dibujar_terreno(pantalla)
            UI.info_velocidad_bala(pantalla, ancho, alto, int(disparo.velocidad_actual))
            self.draw_tank(pantalla)
            tanque_enemigo.draw_tank(pantalla)
            pygame.display.flip()
            pygame.time.delay(10)


class Escribir:
    def escribir_texto(pantalla, texto, fuente, size_fuente, color_fuente, color_fondo, x, y):
        fuente = pygame.font.SysFont(fuente, size_fuente)
        texto = fuente.render(texto, True, color_fuente, color_fondo)
        pantalla.blit(texto, (x, y))


class UI:
    def __init__(self):
        pass

    def info_pre_disparo(self, pantalla, ancho, alto, color_jugador, texto_jugador, angulo, velocidad, tanque_jugador):
        ancho_rectangulo = 800
        alto_rectangulo = 150
        png_angulo = pygame.image.load("img/angulo.png").convert_alpha()
        png_velocidad = pygame.image.load("img/velocidad.png").convert_alpha()
        png_bala60 = pygame.image.load("img/60mm.png").convert_alpha()
        png_bala80 = pygame.image.load("img/80mm.png").convert_alpha()
        png_bala105 = pygame.image.load("img/105mm.png").convert_alpha()
        ancho_rectangulo = 1000
        pygame.draw.rect(surface=pantalla, color=color_jugador,
                rect=(ancho // 2 - ancho_rectangulo // 2, alto - alto_rectangulo,
                    ancho_rectangulo, alto_rectangulo), border_radius=20)
        Escribir.escribir_texto(pantalla, texto_jugador, "Verdana", 30, [255, 255, 255], color_jugador,
                                ancho // 2 - 150, alto  - alto_rectangulo)
        pantalla.blit(png_angulo, (ancho // 2 - ancho_rectangulo // 2 + 30, alto  - 75))
        pantalla.blit(png_velocidad, (ancho // 2 - ancho_rectangulo // 2 + 250, alto  - 75))

        # Tanque con bala 60mm seleccionada
        if tanque_jugador.tipo_bala == 0:
            for i in range(tanque_jugador.municion[tanque_jugador.tipo_bala].unidades):
                pantalla.blit(png_bala60, (ancho // 2 - ancho_rectangulo // 2 + 550 + i * 40, alto  - 90))

        # Tanque con bala 80mm seleccionada
        if tanque_jugador.tipo_bala == 1:
            
            for i in range(tanque_jugador.municion[tanque_jugador.tipo_bala].unidades):
                pantalla.blit(png_bala80, (ancho // 2 - ancho_rectangulo // 2 + 550 + i * 40, alto  - 90))

        # Tanque con bala 105mm seleccionada
        if tanque_jugador.tipo_bala == 2:
            for i in range(tanque_jugador.municion[tanque_jugador.tipo_bala].unidades):
                pantalla.blit(png_bala105, (ancho // 2 - ancho_rectangulo // 2 + 550 + i * 40, alto  - 90))


        Escribir.escribir_texto(pantalla, f"{angulo}°", "Verdana", 30, [255, 255, 255], color_jugador,
                                ancho // 2 - ancho_rectangulo // 2 + 120, alto  - 70)
        Escribir.escribir_texto(pantalla, f"{velocidad} m/s", "Verdana", 30, [255, 255, 255], color_jugador,
                                ancho // 2 - ancho_rectangulo // 2 + 320, alto  - 70)

    def info_post_disparo(self, pantalla, ancho, alto, color_jugador, altura, distancia):
        ancho_rectangulo = 1200
        alto_rectangulo = 150
        png_altura = pygame.image.load("img/altura.png").convert_alpha()
        png_distancia = pygame.image.load("img/distancia.png").convert_alpha()
        pygame.draw.rect(surface=pantalla, color=color_jugador, rect=(
            ancho // 2 - ancho_rectangulo // 2, alto  - alto_rectangulo, ancho_rectangulo, alto_rectangulo),
                         border_radius=20)
        Escribir.escribir_texto(pantalla, f"Información del disparo", "Verdana", 30, [255, 255, 255], color_jugador,
                                ancho // 2 - 180, alto  - alto_rectangulo)
        pantalla.blit(png_altura, (ancho // 2 - ancho_rectangulo // 2 + 130, alto - 75))
        pantalla.blit(png_distancia, (ancho // 2 - ancho_rectangulo // 2 + 640, alto  - 75))
        Escribir.escribir_texto(pantalla, f"{int(altura)} metros", "Verdana", 30, [255, 255, 255], color_jugador,
                                ancho // 2 - ancho_rectangulo // 2 + 220, alto  - 70)
        if distancia != -1:
            Escribir.escribir_texto(pantalla, f"{int(distancia)} metros", "Verdana", 30, [255, 255, 255], color_jugador,
                                    ancho // 2 - ancho_rectangulo // 2 + 720, alto  - 70)
        else:
            Escribir.escribir_texto(pantalla, f"Bala fuera del mapa", "Verdana", 30, [255, 255, 255], color_jugador,
                                    ancho // 2 - ancho_rectangulo // 2 + 790, alto  - 65)
    
    def info_velocidad_bala(pantalla, ancho, alto, velocidad):
        ancho_rectangulo = 600
        alto_rectangulo = 100
        pygame.draw.rect(surface=pantalla, color=(0, 0, 0), rect=(
            ancho // 2 - ancho_rectangulo // 2, alto  - alto_rectangulo, ancho_rectangulo, alto_rectangulo),
                         border_radius=20)
        Escribir.escribir_texto(pantalla, f"Velocidad actual de la bala: {velocidad}m/s", "Verdana", 30, [255, 255, 255], (0, 0, 0),
                    ancho // 2 - ancho_rectangulo // 2 + 10, alto  - 70)
        