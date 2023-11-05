import pygame
import constantes
from Escribir import Escribir


class UI:
    def __init__(self):
        self.png_alerta = pygame.image.load("img/alerta.png").convert_alpha()
        self.png_dinero = pygame.image.load("img/dinero.png").convert_alpha()
        self.png_salud = pygame.image.load("img/salud.png").convert_alpha()
        self.png_angulo = pygame.image.load("img/angulo.png").convert_alpha()
        self.png_velocidad = pygame.image.load("img/velocidad.png").convert_alpha()
        self.png_bala60 = pygame.image.load("img/60mm.png").convert_alpha()
        self.png_bala80 = pygame.image.load("img/80mm.png").convert_alpha()
        self.png_bala105 = pygame.image.load("img/105mm.png").convert_alpha()

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

    def mensaje_caida(self, pantalla, ancho, diff_y):
        ancho_rectangulo = 925
        alto_rectangulo = 70
        pygame.draw.rect(surface=pantalla, color=(0, 0, 0),
                rect=(ancho // 2 - ancho_rectangulo // 2, 10,
                    ancho_rectangulo, alto_rectangulo), border_radius=20)
        Escribir.escribir_texto(pantalla, f"¡El tanque cayó {diff_y} metros y ha recibido {diff_y // 2} de daño extra!", "Verdana", 30, [255, 255, 255], (0, 0, 0), ancho // 2 - ancho_rectangulo // 2 + 10, 25)
    
    def rectangulo(self, pantalla):
        alto_rectangulo = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 5
        pygame.draw.rect(surface=pantalla, color=(50, 50, 50),
                rect=(0, alto_rectangulo, constantes.ANCHO_VENTANA, alto_rectangulo))
        pygame.draw.rect(surface=pantalla, color=(255, 255, 255),
                rect=(0, constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 5, constantes.ANCHO_VENTANA, 20))

    def texto_jugador(self, pantalla, color_jugador, texto_jugador):
        x = 30
        y = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 5.75
        alto_rectangulo = constantes.ALTO_VENTANA // 20
        ancho_rectangulo = constantes.ALTO_VENTANA // 3
        pygame.draw.rect(surface=pantalla, color=color_jugador, rect=(x, y, ancho_rectangulo, alto_rectangulo), border_radius=20)
        Escribir.escribir_texto(pantalla, texto_jugador, "Verdana", 25, constantes.BLANCO, color_jugador,
                    x + ancho_rectangulo // 3.05, y + 10)
        
    def texto_dinero(self, pantalla, dinero):
        x = 30
        y = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 8.2
        pantalla.blit(self.png_dinero, (x, y))
        Escribir.escribir_texto(pantalla, f"${dinero}", "Verdana", 30, constantes.BLANCO, (50, 50, 50),
                    x + (x * 3), y + 10)

    def texto_salud(self, pantalla, salud):
        x = 50
        y = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 20
        x_texto = 30
        y_texto = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 16.4
        pantalla.blit(self.png_salud, (x, y))
        Escribir.escribir_texto(pantalla, f"{int(salud)} HP", "Verdana", 30, constantes.BLANCO, (50, 50, 50),
                    x_texto + (x_texto * 3), y_texto + 10)
        
        
    def texto_ajustes_disparo(self, pantalla):
        x_texto = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // (1.4 + 0.275)
        y_texto = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 6
        Escribir.escribir_texto(pantalla, "Ajustes del disparo", "Verdana", 30, constantes.BLANCO, (50, 50, 50),
                    x_texto, y_texto)
        

    def texto_angulo(self, pantalla, angulo):
        x_texto = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // (1.3 + 0.3 + 0.1)
        y_texto = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 9.5
        x_img = x_texto + constantes.ANCHO_VENTANA // (20 + 0.3)
        y_img = y_texto - constantes.ALTO_VENTANA // 50
        Escribir.escribir_texto(pantalla, "Ángulo:", "Verdana", 20, constantes.BLANCO, (50, 50, 50),
                    x_texto, y_texto)
        pantalla.blit(self.png_angulo, (x_img, y_img))
        x_texto2 = x_texto + constantes.ANCHO_VENTANA // (11 + 0.3)
        y_texto2 = y_texto - 5
        Escribir.escribir_texto(pantalla, angulo, "Verdana", 25, constantes.BLANCO, (50, 50, 50),
                    x_texto2, y_texto2)
        

    def texto_velocidad(self, pantalla, velocidad):
        x_texto = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // (1.28 + 0.3 + 0.1)
        y_texto = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 25
        x_img = x_texto + constantes.ANCHO_VENTANA // (16 + 0.3)
        y_img = y_texto - constantes.ALTO_VENTANA // 50
        Escribir.escribir_texto(pantalla, "Velocidad:", "Verdana", 20, constantes.BLANCO, (50, 50, 50),
                    x_texto, y_texto)
        pantalla.blit(self.png_velocidad, (x_img, y_img))
        x_texto2 = x_texto + constantes.ANCHO_VENTANA // (9.5 + 0.3)
        y_texto2 = y_texto - 5
        Escribir.escribir_texto(pantalla, f"{int(velocidad)} m/s", "Verdana", 25, constantes.BLANCO, (50, 50, 50),
                    x_texto2, y_texto2)
    

    def texto_tipo_bala(self, pantalla, tipo_bala):
        x_texto = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // (6 + 0.3 + 0.1)
        y_texto = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 6
        if tipo_bala == 0:
            texto = "Bala 60mm"
        elif tipo_bala == 1:
            texto = "Bala 80mm"
        else:
            texto = "Bala 105mm"
        Escribir.escribir_texto(pantalla, texto, "Verdana", 25, constantes.BLANCO, (50, 50, 50), x_texto, y_texto)     


    def texto_sin_municion(self, pantalla):
        alto_rectangulo = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 1.075
        ancho_rectangulo = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // 1.2
        x = constantes.ANCHO_VENTANA // 1.25
        y = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 8.5
        color_fondo = (255, 62, 50)
        pygame.draw.rect(surface=pantalla, color=color_fondo,
                rect=(x, y, ancho_rectangulo, alto_rectangulo), border_radius=10)
        pantalla.blit(self.png_alerta, (x + 10, y + 5))
        Escribir.escribir_texto(pantalla, "No hay munición", "Verdana", 25, constantes.BLANCO, color_fondo,
                    x + ancho_rectangulo // 3.9, y + alto_rectangulo // 3.5)
        

    def texto_unidades(self, pantalla, unidades):
        x_texto = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // (6 + 0.3 + 0.1)
        y_texto = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 25
        if unidades != 1:
            Escribir.escribir_texto(pantalla, f"x{unidades} unidades.", "Verdana", 25, constantes.BLANCO, (50, 50, 50), x_texto, y_texto)
        else:
            Escribir.escribir_texto(pantalla, f"x1 unidad.", "Verdana", 25, constantes.BLANCO, (50, 50, 50), x_texto, y_texto)
           

    def cantidad_img_balas(self, pantalla, tipo_bala, unidades):
        if unidades == 0:
            self.texto_sin_municion(pantalla)
        else:
            if tipo_bala == 0:
                bala = self.png_bala60
            elif tipo_bala == 1:
                bala = self.png_bala80
            else:
                bala = self.png_bala105
            bala = pygame.transform.scale(bala, (9.25 * 3, 20 * 3))
            x_primera_bala = constantes.ANCHO_VENTANA // 1.28
            y_primera_bala = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 8.5
            if unidades <= 20:
                for i in range(unidades):
                    pantalla.blit(bala, (x_primera_bala + (20 * i), y_primera_bala))
            else:
                for i in range(20):
                    pantalla.blit(bala, (x_primera_bala + (20 * i), y_primera_bala))
            self.texto_unidades(pantalla, unidades)

