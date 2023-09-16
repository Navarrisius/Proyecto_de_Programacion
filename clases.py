
import pygame
import noise
import random
import math


class Disparo:
    angulo_grados = None
    angulo_radianes = 0
    velocidad_inicial = None
    altura_maxima = None
    distancia_recorrida = None
    radio_bala = 5
    x_bala = None
    y_bala = None
    velocidad_x = None
    velocidad_y = None
    tiempo = 0.1

    def __init__(self, angulo_grados, velocidad_inicial, x, y):
        self.angulo_grados = angulo_grados
        self.velocidad_inicial = velocidad_inicial
        self.angulo_radianes = math.radians(angulo_grados)
        self.velocidad_x = velocidad_inicial * math.cos(self.angulo_radianes)
        self.velocidad_y = - velocidad_inicial * math.sin(self.angulo_radianes)
        self.x_bala = x
        self.y_bala = y


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
    

class Tanque:
    color = None
    posicion_x = None
    posicion_y = None
    vivo = True
    angulo_n = None #Angulo Grados
    angulo_canon = None #Angulo Radianes

    def __init__(self, color):
        self.color = color
    
    def disparar(self, pantalla, color, disparo):
        disparo.x_bala += disparo.velocidad_x * disparo.tiempo
        disparo.y_bala += (disparo.velocidad_y * disparo.tiempo) + (0.5 * 9.81 * disparo.tiempo ** 2)
        disparo.velocidad_y += 9.81 * disparo.tiempo
        pygame.draw.circle(pantalla, color, (int(disparo.x_bala), int(disparo.y_bala)), disparo.radio_bala)
        pygame.display.flip()
        pygame.time.delay(10)