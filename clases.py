
import pygame
import noise
import random
import math


class Disparo:
    angulo_grados = None
    angulo_radianes = 0
    velocidad_inicial = 10
    altura_maxima = None
    distancia_recorrida = None
    radio_bala = 5
    x_bala = None
    y_bala = None
    velocidad_x = None
    velocidad_y = None
    tiempo = 0.1
    impacto_terreno = None
    impacto_tanque = None


    def __init__(self, angulo_grados, velocidad_inicial, x, y):
        self.angulo_grados = angulo_grados
        self.velocidad_inicial = velocidad_inicial
        self.angulo_radianes = math.radians(angulo_grados)
        self.velocidad_x = velocidad_inicial * math.cos(self.angulo_radianes)
        self.velocidad_y = -velocidad_inicial * math.sin(self.angulo_radianes)
        self.x_bala = x
        self.y_bala = y
        self.radio_bala = 5
        self.tiempo = 0.1

    def actualizar(self):
        self.x_bala += self.velocidad_x * self.tiempo
        self.y_bala += (self.velocidad_y * self.tiempo) + (0.5 * 9.81 * (self.tiempo ** 2))
        self.velocidad_y += 9.81 * self.tiempo

    def dibujar(self, pantalla, color):
        pygame.draw.circle(pantalla, color, (int(self.x_bala), int(self.y_bala)), self.radio_bala)



class Jugador:
    nombre = None
    tanque = None
    puede_jugar = False

    def __init__(self, nombre, tanque):
        self.nombre = nombre
        self.tanque = tanque


class Partida:
    en_partida = None

    def __init__(self):
        self.en_partida = True


class Terreno:
    def cargar_fondo(self, screen):
        mountain_png = pygame.image.load("img/Background/mountain.png").convert_alpha()
        screen.blit(mountain_png, (0, 0))

    def generar_terreno(self, x, altura_maxima, width):
        return altura_maxima * math.e ** (-((x - width) ** 2) / (2 * (width / 2) ** 2)) * math.cos(0.01 * (x - width)) + 200
    
    def dibujar_terreno(self, ancho, alto):
        altura_terreno = [0] * ancho
        for x in range(ancho):
            altura_terreno[x] += self.generar_terreno(x, 200, alto)
    

class Tanque:
    color = None
    posicion_x = None
    posicion_y = None
    vivo = True
    angulo_n = None
    angulo_canon = None
    velocidad_disparo = 50

    def __init__(self, color):
        self.color = color
        self.vivo = True

    def verificar_impacto_tanque_enemigo(self, disparo, tanque_enemigo):
        if disparo.y_bala >= tanque_enemigo.posicion_y and (tanque_enemigo.posicion_x - 50 <= disparo.x_bala <= tanque_enemigo.posicion_x + 50):
            return 1
        else:
            return 0

    def disparar(self, pantalla, ancho, alto, terreno, disparo, altura_terreno, tanque_enemigo):
        disparo.x_bala = self.posicion_x
        disparo.y_bala = self.posicion_y
        while disparo.y_bala <= alto - altura_terreno[int(disparo.x_bala)] and disparo.y_bala <= alto:
            terreno.dibujar_terreno(ancho, alto)
            disparo.actualizar()
            disparo.dibujar(pantalla, self.color)
            if disparo.y_bala > alto - altura_terreno[int(disparo.x_bala)]:
                disparo.impacto_terreno = True
                print("IMPACTO CON TERRENO")
                return 0
            if self.verificar_impacto_tanque_enemigo(disparo, tanque_enemigo):
                print("IMPACTO CON TANQUE")
                return 1
            pygame.display.flip()
            pygame.time.delay(10)
    