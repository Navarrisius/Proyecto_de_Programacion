import math, pygame

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
    img_bala = None

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

    def elegir_imagen(self, tipo_municion):
        if tipo_municion == 0:
            self.img_bala = pygame.image.load("img/60mm.png")
        elif tipo_municion == 1:
            self.img_bala = pygame.image.load("img/80mm.png")
        else:
            self.img_bala = pygame.image.load("img/105mm.png")
        self.img_bala = pygame.transform.scale(self.img_bala, (9.25, 20))

    def actualizar(self):
        self.x_bala += self.velocidad_x * self.tiempo
        self.y_bala += (self.velocidad_y * self.tiempo) + (0.5 * 9.81 * (self.tiempo ** 2))
        self.velocidad_y += 9.81 * self.tiempo
        self.eje_x.append(self.x_bala)
        self.eje_y.append(self.y_bala)
        self.velocidad_actual = math.sqrt(self.velocidad_x ** 2 + self.velocidad_y ** 2)

    def dibujar(self, pantalla):
        angulo_rotacion = math.degrees(math.atan2(-self.velocidad_y, self.velocidad_x))
        angulo_rotacion -= 90
        imagen_rotada = pygame.transform.rotate(self.img_bala, angulo_rotacion)
        pantalla.blit(imagen_rotada, (int(self.x_bala - 4.625), int(self.y_bala - 10)))

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
    
    def verificar_impacto_terreno(self, pos, altura_terreno):
        if self.y_bala > 0 and altura_terreno[int(self.y_bala)][int(self.x_bala)] == "x":
            return 0
        else:
            return 1
    
    def recorrido(self, pantalla, color):
        for i in range(len(self.eje_x)):
            pygame.draw.circle(pantalla, color, (int(self.eje_x[i]), int(self.eje_y[i])), 2)
    
    def calcular_damage(self, tanque_enemigo, radio_impacto, ancho):
        if self.impacto_terreno:
            # GUARDA ULTIMA POSICIÓN DE LA BALA (COORDENADA DE IMPACTO)
            coor_x = int(self.eje_x[-1])
            coor_y = int(self.eje_y[-1])

            if coor_x >= 0 and coor_x < ancho:
                coor_x_tanque_enemigo = tanque_enemigo.posicion_x
                coor_y_tanque_enemigo = tanque_enemigo.posicion_y

                distancias = []
                distancias.append(math.sqrt((coor_x_tanque_enemigo - coor_x) ** 2 + (coor_y_tanque_enemigo - 10 - coor_y) ** 2))
                distancias.append(math.sqrt((coor_x_tanque_enemigo + 30 - coor_x) ** 2 + (coor_y_tanque_enemigo - 10- coor_y) ** 2))
                distancias.append(math.sqrt((coor_x_tanque_enemigo - 30 - coor_x) ** 2 + (coor_y_tanque_enemigo - 10- coor_y) ** 2))
                distancias_validas = [dist for dist in distancias if dist < radio_impacto]

                if distancias_validas:
                    mayor_distancia_valida = max(distancias_validas)
                    return mayor_distancia_valida
                else:
                    return 0
            else:
                return 0
        else:
            return 0