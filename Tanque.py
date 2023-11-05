import math, pygame
from Bala import Bala
from Fondo import Fondo
from UI import UI


class Tanque:
    municion = None
    balas = None
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
    caida_tanque = None
    
    def __init__(self, color):
        self.municion = [Bala(0), Bala(1), Bala(2)]
        self.balas = 16
        self.color = color
        self.tipo_bala = 0
        self.angulo_canon = 90
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
        elif color == (252, 3, 186):
            self.imagen = pygame.image.load("img/tanque_rojo.png").convert_alpha()

    def corregir_salud(self):
        if self.salud <= 0:
            self.salud = 0

    def draw_tank(self, pantalla):
        turret_length = 30
        turret_start = (self.posicion_x - 5, self.posicion_y - 25)
        self.turret_end = (self.posicion_x - 5 + turret_length * math.cos(self.angulo_canon),
                           self.posicion_y - 25 - turret_length * math.sin(self.angulo_canon))
        pygame.draw.line(pantalla, "gray", turret_start, self.turret_end, 4)

        pantalla.blit(self.imagen, (self.posicion_x - 40, self.posicion_y - 40))

    def disparar(self, pantalla, ancho, alto, terreno, disparo, altura_terreno, tanques_enemigos):
        disparo.elegir_imagen(self.tipo_bala)
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
            disparo.dibujar(pantalla)
            disparo.dibujar_indicador(pantalla, self.color)
            try:
                if not disparo.verificar_impacto_terreno(altura_terreno):
                    disparo.impacto_terreno = True
                    disparo.calcular_distancia_maxima(self.posicion_x)
                    return 0
            # BALA FUERA DEL MAPA
            except IndexError:
                pass
            # IMPACTO CON TANQUE ENEMIGO
            for tanque in tanques_enemigos :
                if disparo.verificar_impacto_tanque_enemigo(tanque):
                    disparo.impacto_tanque = True
                    disparo.calcular_distancia_maxima(self.posicion_x)
                    return 1
            # IMPACTO CON TANQUE PROPIO
            if disparo.verificar_impacto_tanque_enemigo(self):
                disparo.impacto_tanque = True
                disparo.calcular_distancia_maxima(self.posicion_x)
                return -1
            terreno.dibujar_terreno(pantalla)
            UI.info_velocidad_bala(pantalla, ancho, alto, int(disparo.velocidad_actual))
            self.draw_tank(pantalla)
            tanque_enemigo.draw_tank(pantalla)
            pygame.display.flip()
            pygame.time.delay(10)
    
    def calcular_damage_caida(self, pos_y_anterior):
        diff_y = abs(self.posicion_y - pos_y_anterior) // 2
        self.salud -= diff_y