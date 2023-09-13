
import pygame
import noise
import random
import math


class Disparo:
    angulo = None
    velocidad_inicial = None
    altura_maxima = None
    distancia_recorrida = None

    def __init__(self, angulo, velocidad_inicial):
        self.angulo = angulo
        self.velocidad_inicial = velocidad_inicial
    
    def dibujar_disparo(self):
        '''
        TODO: Dibujar trayectoria del disparo y mostrar la altura máxima alcanzada y la distancia recorrida
        '''
        pass

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

    def cargar_fondo(self, screen):
        mountain_png = pygame.image.load("img/Background/mountain.png").convert_alpha()
        screen.blit(mountain_png, (0, 0))

    def generar_terreno(self,x, altura_maxima, width):
        return altura_maxima * math.e ** (-((x - width) ** 2) / (2 * (width / 2) ** 2)) * math.cos(0.01 * (x - width)) + 200
    
class Tanque:
    color = None
    posicion_x = None
    posicion_y = None
    vivo = True

    def __init__(self, color):
        self.color = color
    
    def disparar(self, pos_x, pos_y, angulo, velocidad_inicial):
        '''
        Fórmula trayectoria balística
        g = gravedad
        a = angulo
        v = velocidad inicial
        y = x * tan(a) - (g * x^2 / 2 * v * cos^2(a))
        '''
        GRAVEDAD = 9.8