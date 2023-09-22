import pygame
import math


class Disparo:
    angulo_grados = None
    angulo_radianes = 0
    velocidad_inicial = None
    velocidad_actual = 0
    altura_maxima = 0
    distancia_maxima = 0
    radio_bala = 5
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

    def __init__(self, angulo_grados, velocidad_inicial, autor):
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
        pygame.draw.circle(pantalla, color, (int(self.x_bala), int(self.y_bala)), self.radio_bala)
        Escribir.escribir_texto(pantalla=pantalla, texto="Velocidad actual de la bala: " + str(int(self.velocidad_actual)) + " m/s", fuente="Consolas", color_fuente=(255, 255, 255), size_fuente=25, color_fondo=(0,0,0), x=ancho // 2, y=alto // 6 + 56)
    
    def calcular_altura_maxima(self):
        self.altura_maxima = abs((self.velocidad_inicial ** 2 * (math.sin(self.angulo_radianes) ** 2)) / (2 * 9.81))
    
    def calcular_distancia_maxima(self, tanque_posicion_x):
        self.distancia_maxima = abs(self.x_bala - self.distancia_maxima - tanque_posicion_x)

    def recorrido(self, pantalla):
        for i in range(len(self.eje_x)):
            pygame.draw.circle(pantalla, (0, 0, 0), (int(self.eje_x[i]), int(self.eje_y[i])), 2)


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

    def cargar_fondo(self, screen):
        mountain_png = pygame.image.load("img/Background/mountain.png").convert_alpha()
        screen.blit(mountain_png, (0, 0))
        
class Terreno:
    def generar_terreno(self, x, altura_maxima, width):
        return altura_maxima * math.e ** (-((x - width) ** 2) / (2 * (width / 2) ** 2)) * math.cos(0.01 * (x - width)) + 200
    
    def dibujar_terreno(self, pantalla, ancho, alto):
        altura_terreno = [0] * ancho
        for x in range(ancho):
            altura_terreno[x] += self.generar_terreno(x, 200, alto)
        for x in range(ancho):
            pygame.draw.rect(pantalla, (220, 220, 220), (x, alto - altura_terreno[x], 1, altura_terreno[x]))
        for x in range(ancho):
            pygame.draw.rect(pantalla, (173,204,246), (x, alto - altura_terreno[x] + 10, 1, altura_terreno[x]))
        for x in range(ancho):
            pygame.draw.rect(pantalla, (175,209,249), (x, alto - altura_terreno[x] + 150, 1, altura_terreno[x]))
        for x in range(ancho):
            pygame.draw.rect(pantalla, (178,214,250), (x, alto - altura_terreno[x] + 300, 1, altura_terreno[x]))

class Fondo:
    mountain_png = None

    def __init__(self):
        self.mountain_png = pygame.image.load("img/mountain.png").convert_alpha()

    def cargar_fondo(self, screen):
        screen.blit(self.mountain_png, (0, 0))

class Tanque:
    color = None
    posicion_x = None
    posicion_y = None
    vivo = True
    angulo_n = None
    angulo_canon = None
    velocidad_disparo = 50
    turret_end = None

    def __init__(self, color):
        self.color = color
        self.vivo = True

    def draw_tank(self, pantalla):
        tank_points = [(self.posicion_x - 50 // 2, self.posicion_y),(self.posicion_x - 50 // 2, self.posicion_y - 10),
                           (self.posicion_x - 50 // 2 + 5, self.posicion_y - 13),(self.posicion_x + 50 // 2 - 5, self.posicion_y - 13),
                           (self.posicion_x + 50 // 2, self.posicion_y - 10),(self.posicion_x + 50 // 2, self.posicion_y)]
        pygame.draw.polygon(pantalla, self.color, tank_points)
        # Dibuja la torreta del tanque
        turret_length = 30
        turret_start = (self.posicion_x, self.posicion_y - 10)
        self.turret_end = (self.posicion_x + turret_length * math.cos(self.angulo_canon),self.posicion_y - 10 - turret_length * math.sin(self.angulo_canon))
        pygame.draw.line(pantalla, "gray", turret_start, self.turret_end, 4)

    def verificar_impacto_tanque_enemigo(self, disparo, tanque_enemigo):
        if (disparo.y_bala >= tanque_enemigo.posicion_y - 20) and (tanque_enemigo.posicion_x - 27 <= disparo.x_bala <= tanque_enemigo.posicion_x + 27):
            return 1
        else:
            return 0

    def disparar(self, pantalla, ancho, alto, terreno, disparo, altura_terreno, tanque_enemigo):
        disparo.x_bala = self.turret_end[0]
        disparo.y_bala = self.turret_end[1]
        disparo.x_inicial = self.turret_end[0]
        disparo.calcular_altura_maxima()
        fondo = Fondo()
        while True:
            fondo.cargar_fondo(pantalla)

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
                if disparo.y_bala > alto - altura_terreno[int(disparo.x_bala)] - 5:
                    disparo.impacto_terreno = True
                    disparo.calcular_distancia_maxima(self.posicion_x)
                    return 0
            # BALA FUERA DEL MAPA
            except IndexError:
                None
            # IMPACTO CON TANQUE ENEMIGO
            if self.verificar_impacto_tanque_enemigo(disparo, tanque_enemigo):
                disparo.impacto_tanque = True
                disparo.calcular_distancia_maxima(self.posicion_x)
                return 1
            terreno.dibujar_terreno(pantalla, ancho, alto)
            self.draw_tank(pantalla)
            tanque_enemigo.draw_tank(pantalla)
            pygame.display.flip()
            pygame.time.delay(10)

class Escribir:
    def escribir_texto(pantalla, texto, fuente, size_fuente, color_fuente, color_fondo, x, y):
        fuente = pygame.font.SysFont(fuente, size_fuente)
        texto = fuente.render(texto, True, color_fuente, color_fondo)
        pantalla.blit(texto, (x, y))
    