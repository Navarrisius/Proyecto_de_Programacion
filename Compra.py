import pygame
import constantes
from Boton import Boton
from Escribir import Escribir
ancho_botón, altura_botón = 0.10, 0.04
margin_ratio = 0.05
def texto_dinero_compra(self, pantalla, dinero):
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_dinero = pygame.transform.scale(self.png_dinero, (30, 40))
        pantalla.blit(self.png_dinero, posicion(-0.034,0.57,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla,f"${dinero}",(0.05 + ancho_botón / 2, 0.6 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO,"Verdana")
def texto_tipo_bala_compra(pantalla, tipo_bala):
        if tipo_bala == 0:
            texto = "Bala 60mm"
        elif tipo_bala == 1:
            texto = "Bala 80mm"
        else:
            texto = "Bala 105mm"
        Escribir.render_text(pantalla, texto,(0.445 + ancho_botón / 2, 0.37 - 0.5 * altura_botón + margin_ratio),20, constantes.BLANCO,"Verdana")
def texto_jugador_compra(self, pantalla, color_jugador, texto_jugador):
        x = 30
        y = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 2
        alto_rectangulo = constantes.ALTO_VENTANA // 15
        ancho_rectangulo = constantes.ALTO_VENTANA // 3
        pygame.draw.rect(surface=pantalla, color=color_jugador, rect=(x, y, ancho_rectangulo, alto_rectangulo), border_radius=20)
        Escribir.render_text(pantalla, texto_jugador,(0.05 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio),20, constantes.BLANCO, "verdana")
def posicion(x,y,ancho_botón,altura_botón,margin_ratio):
        pos_x_rel = x + ancho_botón / 2
        pos_y_rel = y - 0.5 * altura_botón + margin_ratio
        pos_x = constantes.ANCHO_VENTANA * pos_x_rel
        pos_y = constantes.ALTO_VENTANA * pos_y_rel
        return pos_x, pos_y
def texto_sin_municion_compra(self, pantalla):
    alto_rectangulo = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 1.075
    ancho_rectangulo = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // 1.2
    x = constantes.ANCHO_VENTANA // 2.4
    y = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 2
    color_fondo = (255, 62, 50)
    pygame.draw.rect(surface=pantalla, color=color_fondo,
            rect=(x, y, ancho_rectangulo, alto_rectangulo), border_radius=10)
    if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
        self.png_alerta = pygame.transform.scale(self.png_alerta, (23,43))
    pantalla.blit(self.png_alerta, posicion(0.37,0.48,ancho_botón,altura_botón,margin_ratio))
    Escribir.render_text(pantalla,"No hay munición",(0.47 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana")

def texto_unidades_compra(pantalla, unidades):
    if unidades != 1:
        Escribir.render_text(pantalla, f"x{unidades} unidades.",(0.45 + ancho_botón / 2, 0.6 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana") 
    else:
        Escribir.render_text(pantalla, f"x1 unidad.",(0.45 + ancho_botón / 2, 0.6 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana") 


def cantidad_img_balas_compra(self, pantalla, tipo_bala, unidades):
    if unidades == 0:
        texto_sin_municion_compra(self,pantalla)
    else:
        if tipo_bala == 0:
            bala = self.png_bala60
        elif tipo_bala == 1:
            bala = self.png_bala80
        else:
            bala = self.png_bala105
        bala = pygame.transform.scale(bala, (9.25 * 3, 20 * 3))
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            bala = pygame.transform.scale(bala, (15, 40))
        x_primera_bala = constantes.ANCHO_VENTANA // 2.3
        y_primera_bala = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 2
        if unidades <= 20:
            for i in range(unidades):
                pantalla.blit(bala, (x_primera_bala + (18 * i), y_primera_bala))
        else:
            for i in range(20):
                pantalla.blit(bala, (x_primera_bala + (18 * i), y_primera_bala))
        texto_unidades_compra(pantalla, unidades)
class Compra:
    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game
        
    def run(self,turno):
        ancho_botón, altura_botón = 0.15, 0.08
        margin_ratio = 0.05  # Margen de separación entre botones
        botones = [
            Boton(0.18 - ancho_botón / 2, 0.8 + 0.5 * altura_botón , ancho_botón,
                altura_botón, "Comprar",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
            Boton(0.38 - ancho_botón / 2, 0.8 + 0.5 * altura_botón, ancho_botón, altura_botón, "Vender",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
            Boton(0.58 - ancho_botón / 2, 0.8 + 0.5 * altura_botón , ancho_botón,
                altura_botón, "Cambiar",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
            Boton(0.78 - ancho_botón / 2, 0.8 + 0.5 * altura_botón, ancho_botón,
                altura_botón, "Listo", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
        ]
        # Bucle principal
        running = True
        while running:
            self.pantalla.fill((1, 30, 97))
            Escribir.render_text(self.pantalla, f"Tiempo de compra - Partida {constantes.RONDA_ACTUAL}", (0.42 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.BLANCO, "More Sugar")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if botones[0].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        sound = pygame.mixer.Sound('mp3/sonido_compra.mp3')
                        sound.set_volume(0.2)
                        if turno.tanque.tipo_bala == 0 and turno.dinero >= 1000:
                            turno.comprar_bala_60mm()
                            sound.play()
                        if turno.tanque.tipo_bala == 1 and turno.dinero >= 2500:
                            turno.comprar_bala_80mm()
                            sound.play()
                        if turno.tanque.tipo_bala == 2 and turno.dinero >= 4000:
                            turno.comprar_bala_105mm()
                            sound.play()
                    if botones[1].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        sound = pygame.mixer.Sound('mp3/sonido_venta.mp3')
                        sound.set_volume(0.2)
                        if turno.tanque.tipo_bala == 0 and turno.tanque.municion[0].unidades > 0:
                            turno.vender_bala_60mm()
                            sound.play()
                        if turno.tanque.tipo_bala == 1 and turno.tanque.municion[1].unidades > 0:
                            turno.vender_bala_80mm()
                            sound.play()
                        if turno.tanque.tipo_bala == 2 and turno.tanque.municion[2].unidades > 0:
                            turno.vender_bala_105mm()
                            sound.play()
                    if botones[2].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        if turno.tanque.tipo_bala < 2:
                            turno.tanque.tipo_bala += 1
                        else:
                            turno.tanque.tipo_bala = 0
                    if botones[3].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        constantes.TURNO_ACTUAL += 1
                        running = False
            texto_tipo_bala_compra(self.pantalla, turno.tanque.tipo_bala)
            cantidad_img_balas_compra(self,self.pantalla, turno.tanque.tipo_bala, turno.tanque.municion[turno.tanque.tipo_bala].unidades)
            texto_jugador_compra(self,self.pantalla, turno.tanque.color, turno.nombre)
            texto_dinero_compra(self,self.pantalla, turno.dinero)
            for boton in botones:
                boton.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)


            pygame.display.flip()