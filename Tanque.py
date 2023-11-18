import math, pygame, constantes
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
    angulo_n = 0
    angulo_canon = None
    velocidad_disparo = 50
    turret_end = None
    imagen = None
    caida_tanque = None
    dano_caida = None
    
    def __init__(self, color):
        self.municion = [Bala(0), Bala(1), Bala(2)]
        self.balas = 0
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
            self.imagen = pygame.image.load("img/tanque_rosado.png").convert_alpha()


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


    def disparar(self, pantalla, ancho, alto, terreno, disparo, altura_terreno, tanques):
        disparo.elegir_imagen(self.tipo_bala)
        disparo.x_bala = self.turret_end[0]
        disparo.y_bala = self.turret_end[1]
        disparo.x_inicial = self.turret_end[0]
        disparo.calcular_altura_maxima()
        fondo = Fondo()
        ui = UI()
        altura_alcanzada = False
        while True:
            altura = self.turret_end[1] - disparo.y_bala
            fondo.cargar_fondo(pantalla, 1)
            # Si la bala sale de los limites laterales de la pantalla
            if disparo.x_bala >= ancho:
                disparo.distancia_maxima = -1
                return -1
            if disparo.x_bala <= 0:
                disparo.distancia_maxima = -1
                return -1
            disparo.actualizar_dibujo(pantalla, self.color)
            try:
                if not disparo.verificar_impacto_terreno(altura_terreno):
                    disparo.impacto_terreno = True
                    tanque_danyado = disparo.realizar_damage_tanque(self.municion[self.tipo_bala])
                    disparo.calcular_distancia_maxima(self.posicion_x)
                    if tanque_danyado != -1:
                        return tanque_danyado
                    else:
                        return -1
            except IndexError:
                disparo.distancia_maxima = -1
            # IMPACTO CON TANQUE
            for tanque in tanques:
                if disparo.verificar_impacto_tanque_enemigo(tanque):
                    disparo.impacto_tanque = True
                    tanque.salud -= self.municion[self.tipo_bala].dano
                    disparo.calcular_distancia_maxima(self.posicion_x - 5)
                    return tanque
            terreno.dibujar_terreno(pantalla)
            ui.barras_de_salud(pantalla)
            if altura >= disparo.altura_maxima - 1:
                altura_alcanzada = True
            if altura_alcanzada:
                ui.info_bala(pantalla, int(disparo.velocidad_actual), int(disparo.altura_maxima), 0)
            else:
                ui.info_bala(pantalla, int(disparo.velocidad_actual), 0, 0)
            for tanque in tanques:
                tanque.draw_tank(pantalla)
            pygame.display.flip()


    def calcular_damage_caida(self, pos_y_anterior):
        diff_y = abs(self.posicion_y - pos_y_anterior) // 2
        self.dano_caida = int(diff_y * (constantes.GRAVEDAD / 10))
        self.salud -= self.dano_caida
        self.corregir_salud()