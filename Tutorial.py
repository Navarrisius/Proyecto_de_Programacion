import pygame
import constantes
import funciones
from Escribir import Escribir
from Boton import Boton

class Tutorial:
    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game

    
    def run(self):
        en_tuto = True
        nuevo_ancho = 100
        nuevo_alto = 100
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            nuevo_alto = 50
            nuevo_ancho = 55
        ancho_botón, altura_botón = 0.10, 0.04
        margin_ratio = 0.05  # Margen de separación entre botones
        Volver = Boton(0.36 + ancho_botón / 2, 0.65 + 0.5 * altura_botón + margin_ratio, 0.18, 0.10, "Volver", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
        while en_tuto:
            mouse = pygame.mouse.get_pos()
            self.pantalla.fill((219, 241, 243))
            Volver.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
            Escribir.render_text(self.pantalla, "Controles", (0.47 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.NEGRO, "More Sugar")
            png_bala60 = pygame.image.load("img/60mm.png").convert_alpha()
            self.pantalla.blit(png_bala60, funciones.posicion(0.60,0.17,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Bala 60mm", (0.70 + ancho_botón / 2, 0.18 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            Escribir.render_text(self.pantalla, "Costo $1000", (0.705 + ancho_botón / 2, 0.22 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            Escribir.render_text(self.pantalla, "Daño 30", (0.688 + ancho_botón / 2, 0.26 - 0.5 * altura_botón + margin_ratio), 25, constantes.NEGRO, "More Sugar")
            png_bala80 = pygame.image.load("img/80mm.png").convert_alpha()
            self.pantalla.blit(png_bala80, funciones.posicion(0.60,0.375,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Bala 80mm", (0.70 + ancho_botón / 2, 0.385 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            Escribir.render_text(self.pantalla, "Costo $2500", (0.705 + ancho_botón / 2, 0.425 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            Escribir.render_text(self.pantalla, "Daño 40", (0.688 + ancho_botón / 2, 0.465 - 0.5 * altura_botón + margin_ratio), 25, constantes.NEGRO, "More Sugar")
            png_bala105 = pygame.image.load("img/105mm.png").convert_alpha()
            self.pantalla.blit(png_bala105, funciones.posicion(0.60,0.545,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Bala 105mm", (0.705 + ancho_botón / 2, 0.555 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            Escribir.render_text(self.pantalla, "Costo $4000", (0.705 + ancho_botón / 2, 0.59 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            Escribir.render_text(self.pantalla, "Daño 50", (0.688 + ancho_botón / 2, 0.63 - 0.5 * altura_botón + margin_ratio), 25, constantes.NEGRO, "More Sugar")
            
            png_tecla_w = pygame.image.load("img/tecla_w_.png").convert_alpha()
            png_tecla_w_ajustado = pygame.transform.scale(png_tecla_w, (nuevo_ancho, nuevo_alto))
            self.pantalla.blit(png_tecla_w_ajustado, funciones.posicion(-0.017,0.20,ancho_botón,altura_botón,margin_ratio))
            png_tecla_s = pygame.image.load("img/tecla_s_.png").convert_alpha()
            png_tecla_s_ajustado = pygame.transform.scale(png_tecla_s, (nuevo_ancho, nuevo_alto))
            self.pantalla.blit(png_tecla_s_ajustado,  funciones.posicion(-0.017,0.10,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Aumento o disminución de la potencia", (0.3 + ancho_botón / 2, 0.195 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            
            png_tecla_a = pygame.image.load("img/tecla_a_.png").convert_alpha()
            png_tecla_a_ajustado = pygame.transform.scale(png_tecla_a, (nuevo_ancho, nuevo_alto))
            self.pantalla.blit(png_tecla_a_ajustado,  funciones.posicion(-0.04,0.35,ancho_botón,altura_botón,margin_ratio))
            png_tecla_d = pygame.image.load("img/tecla_d_.png").convert_alpha()
            png_tecla_d_ajustado = pygame.transform.scale(png_tecla_d, (nuevo_ancho, nuevo_alto))
            self.pantalla.blit(png_tecla_d_ajustado,  funciones.posicion(0.025,0.35,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Aumento o disminución  del ángulo", (0.28 + ancho_botón / 2, 0.40 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            
            png_tecla_q = pygame.image.load("img/tecla_q.png").convert_alpha()
            png_tecla_q_ajustado = pygame.transform.scale(png_tecla_q, (nuevo_ancho, nuevo_alto))
            self.pantalla.blit(png_tecla_q_ajustado, funciones.posicion(-0.017,0.50,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Cambio de munición", (0.205 + ancho_botón / 2, 0.55 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")
            
            png_tecla_espacio = pygame.image.load("img/Space.png").convert_alpha()
            png_tecla_espacio_ajustado = pygame.transform.scale(png_tecla_espacio, (nuevo_ancho, nuevo_alto))
            self.pantalla.blit(png_tecla_espacio_ajustado, funciones.posicion(-0.017,0.65,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Disparar", (0.145 + ancho_botón / 2, 0.69 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")


            png_tecla_shift = pygame.image.load("img/SHIFT.png").convert_alpha()
            png_tecla_shift_ajustado = pygame.transform.scale(png_tecla_shift, (nuevo_ancho, nuevo_alto))
            self.pantalla.blit(png_tecla_shift_ajustado, funciones.posicion(-0.017,0.80,ancho_botón,altura_botón,margin_ratio))
            Escribir.render_text(self.pantalla, "Aumento o dismunición más rápida ", (0.28 + ancho_botón / 2, 0.85 - 0.5 * altura_botón + margin_ratio), 24, constantes.NEGRO, "More Sugar")

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Volver.si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                            constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA = constantes.DIMENSIONES[0], \
                            constantes.DIMENSIONES[1]
                            self.gameStateManager.set_estado('menu')
                            en_tuto = False

            pygame.display.update()