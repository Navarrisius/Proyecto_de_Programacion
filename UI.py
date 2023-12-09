import pygame
import constantes
from Escribir import Escribir

ancho_botón, altura_botón = 0.10, 0.04
margin_ratio = 0.05

def posicion(x,y,ancho_botón,altura_botón,margin_ratio):
        pos_x_rel = x + ancho_botón / 2
        pos_y_rel = y - 0.5 * altura_botón + margin_ratio
        pos_x = constantes.ANCHO_VENTANA * pos_x_rel
        pos_y = constantes.ALTO_VENTANA * pos_y_rel
        return pos_x, pos_y

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
        self.png_kills = pygame.image.load("img/kills.png").convert_alpha()
        self.png_viento = pygame.image.load("img/viento.png").convert_alpha()
        self.flecha_izquierda = pygame.image.load("img/flecha_izquierda.png").convert_alpha()
        self.flecha_derecha = pygame.image.load("img/flecha_derecha.png").convert_alpha()
        self.flecha_izquierda = pygame.transform.scale(self.flecha_izquierda, (50, 50))
        self.flecha_derecha = pygame.transform.scale(self.flecha_derecha, (50, 50))


    def mensaje_caida(self, pantalla, ancho, diff_y, dano):
        ancho_rectangulo = 925
        alto_rectangulo = 70
        pygame.draw.rect(surface=pantalla, color=(0, 0, 0),
                rect=(ancho // 2 - ancho_rectangulo // 2, 10,
                    ancho_rectangulo, alto_rectangulo), border_radius=20)
        Escribir.escribir_texto(pantalla, f"¡El tanque cayó {diff_y} metros y ha recibido {dano} de daño extra!", "Verdana", 30, [255, 255, 255], (0, 0, 0), ancho // 2 - ancho_rectangulo // 2 + 10, 25)
    

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
        Escribir.render_text(pantalla, texto_jugador,(0.05 + ancho_botón / 2, 0.82 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO, "verdana")
        
    def texto_dinero(self, pantalla, dinero):
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_dinero = pygame.transform.scale(self.png_dinero, (30, 40))
        pantalla.blit(self.png_dinero, posicion(-0.034,0.85,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla,f"${dinero}",(0.05 + ancho_botón / 2, 0.88 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO,"Verdana")

    def texto_salud(self, pantalla, salud):
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_salud = pygame.transform.scale(self.png_salud, (20, 20))
        pantalla.blit(self.png_salud, posicion(-0.02,0.92,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla,f"{int(salud)} HP",(0.05 + ancho_botón / 2, 0.935 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO,"Verdana")
        
        
    def texto_ajustes_disparo(self, pantalla):
        Escribir.render_text(pantalla,  "Ajustes del disparo",(0.42 + ancho_botón / 2, 0.82 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO,"Verdana")
        

    def texto_angulo(self, pantalla, angulo):
        Escribir.render_text(pantalla,"Ángulo:",(0.38 + ancho_botón / 2, 0.88 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana")
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_angulo = pygame.transform.scale(self.png_angulo, (23,43))
        pantalla.blit(self.png_angulo, posicion(0.41,0.84,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla,f"{round(angulo, 1)}°",(0.465 + ancho_botón / 2, 0.88 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana")
        

    def texto_velocidad(self, pantalla, velocidad):
        Escribir.render_text(pantalla,"Velocidad:",(0.373 + ancho_botón / 2, 0.94 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana")
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_velocidad = pygame.transform.scale(self.png_velocidad, (23, 45))
        pantalla.blit(self.png_velocidad, posicion(0.41,0.91,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla,f"{int(velocidad)} m/s",(0.48 + ancho_botón / 2, 0.94 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana")
    

    def texto_tipo_bala(self, pantalla, tipo_bala):
        if tipo_bala == 0:
            texto = "Bala 60mm"
        elif tipo_bala == 1:
            texto = "Bala 80mm"
        else:
            texto = "Bala 105mm"
        Escribir.render_text(pantalla, texto,(0.83 + ancho_botón / 2, 0.82 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO,"Verdana") 


    def texto_sin_municion(self, pantalla):
        alto_rectangulo = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 1.075
        ancho_rectangulo = constantes.ANCHO_VENTANA - constantes.ANCHO_VENTANA // 1.2
        x = constantes.ANCHO_VENTANA // 1.25
        y = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 8.5
        color_fondo = (255, 62, 50)
        pygame.draw.rect(surface=pantalla, color=color_fondo,
                rect=(x, y, ancho_rectangulo, alto_rectangulo), border_radius=10)
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_alerta = pygame.transform.scale(self.png_alerta, (23,43))
        pantalla.blit(self.png_alerta, posicion(0.753,0.857,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla,"No hay munición",(0.85 + ancho_botón / 2, 0.885 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO,"Verdana")

    def texto_unidades(self, pantalla, unidades):
        if unidades != 1:
            Escribir.render_text(pantalla, f"x{unidades} unidades.",(0.83 + ancho_botón / 2, 0.945 - 0.5 * altura_botón + margin_ratio),10, constantes.BLANCO,"Verdana") 
        else:
            Escribir.render_text(pantalla, f"x1 unidad.",(0.83 + ancho_botón / 2, 0.945 - 0.5 * altura_botón + margin_ratio),10, constantes.BLANCO,"Verdana") 
  

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
            if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
                bala = pygame.transform.scale(bala, (15, 40))
            x_primera_bala = constantes.ANCHO_VENTANA // 1.28
            y_primera_bala = constantes.ALTO_VENTANA - constantes.ALTO_VENTANA // 8.5
            if unidades <= 20:
                for i in range(unidades):
                    pantalla.blit(bala, (x_primera_bala + (18 * i), y_primera_bala))
            else:
                for i in range(20):
                    pantalla.blit(bala, (x_primera_bala + (18 * i), y_primera_bala))
            self.texto_unidades(pantalla, unidades)


    def barras_de_salud(self, pantalla):
        for tanque in constantes.TANQUES:
            if tanque.salud > 75:
                color_de_salud_del_jugador = (0, 143, 57)
            elif tanque.salud > 50:
                color_de_salud_del_jugador = (255, 255, 0)
            else:
                color_de_salud_del_jugador = (255, 0, 0)

            pygame.draw.rect(pantalla, (0, 0, 0), (tanque.posicion_x - 59, tanque.posicion_y + 13, 104, 24))
            pygame.draw.rect(pantalla, color_de_salud_del_jugador, (tanque.posicion_x - 57, tanque.posicion_y + 15, tanque.salud, 20))

    
    def info_bala(self, pantalla, velocidad, altura, distancia):
        self.rectangulo(pantalla)
        if velocidad != -1:
            Escribir.render_text(pantalla, "Velocidad Actual del disparo",(0.1 + ancho_botón / 2, 0.814 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
            Escribir.render_text(pantalla, f"{velocidad} m/s.",(0.1 + ancho_botón / 2, 0.87 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
        if altura != 0:
            Escribir.render_text(pantalla, "Altura máxima del disparo",(0.43 + ancho_botón / 2, 0.814 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
            Escribir.render_text(pantalla, f"{altura} m.",(0.43 + ancho_botón / 2, 0.87 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
        if distancia != -1 and distancia != 0:
            Escribir.render_text(pantalla, "Distancia máxima del disparo",(0.73 + ancho_botón / 2, 0.814 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
            Escribir.render_text(pantalla, f"{distancia} m.",(0.73 + ancho_botón / 2, 0.87 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
        elif distancia == 0:
            pass
        else:
            Escribir.render_text(pantalla, "Distancia máxima del disparo",(0.73 + ancho_botón / 2, 0.814 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
            Escribir.render_text(pantalla, f"Bala fuera del mapa",(0.73 + ancho_botón / 2, 0.87 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")

    
    def esperar(self, tiempo):
        pygame.display.update()
        # Esperar 2 segundos
        tiempo_inicial = pygame.time.get_ticks()
        tiempo_espera = tiempo * 1000
        while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
            pass
        pygame.display.flip()

    def ronda_compra(self, pantalla, ancho):
        ancho_rectangulo = 600
        alto_rectangulo = 70
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            ancho_rectangulo = 240
            alto_rectangulo = 40
        pygame.draw.rect(surface=pantalla, color=(0, 0, 0),
                rect=(ancho // 2 - ancho_rectangulo // 2, 10,
                    ancho_rectangulo, alto_rectangulo), border_radius=20)
        Escribir.render_text(pantalla, f"Tiempo de compra - Partida {constantes.RONDA_ACTUAL}",(0.45 + ancho_botón / 2, 0.01 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO, "verdana")

    
    def ronda_actual(self, pantalla):
        Escribir.render_text(pantalla, f"Partida {constantes.RONDA_ACTUAL}",(0.2 + ancho_botón / 2, 0.82 - 0.5 * altura_botón + margin_ratio),15, constantes.BLANCO, "verdana")
        
    
    def kills(self, pantalla, kills):
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_kills = pygame.transform.scale(self.png_kills, (20, 20))
        pantalla.blit(self.png_kills, posicion(0.165,0.865,ancho_botón,altura_botón,margin_ratio))
        if kills == 1:
            Escribir.render_text(pantalla,f"{kills} kill",(0.208 + ancho_botón / 2, 0.877 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")
        else:
            Escribir.render_text(pantalla,f"{kills} kills",(0.208 + ancho_botón / 2, 0.877 - 0.5 * altura_botón + margin_ratio),12, constantes.BLANCO, "verdana")

    
    def pantalla_ganador(self, jugador):
        if jugador != -1:
            nombre = jugador.nombre
            kills = jugador.kills
            if kills == 1:
                print(f"Gana {nombre} con 1 kill")
            else:
                print(f"Gana {nombre} con {kills} kills")
        else:
            print("Empate")

    def indicador_viento(self, pantalla):
        ancho_rectangulo = 240
        alto_rectangulo = 120
        if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
            self.png_viento = pygame.transform.scale(self.png_viento, (20, 20))
            self.flecha_izquierda = pygame.transform.scale(self.flecha_izquierda, (20, 20))
            self.flecha_derecha = pygame.transform.scale(self.flecha_derecha, (20, 20))
        #pygame.draw.rect(surface=pantalla, color=(0, 0, 0), rect=(0, 0, ancho_rectangulo, alto_rectangulo))
        pantalla.blit(self.png_viento, posicion(-0.043,0.02,ancho_botón,altura_botón,margin_ratio))
        Escribir.render_text(pantalla,f"{abs(constantes.VELOCIDAD_VIENTO)} m/s",(0.028 + ancho_botón / 2, 0.015 - 0.5 * altura_botón + margin_ratio),15, (0, 64, 202), "verdana bold")
        if constantes.VELOCIDAD_VIENTO < 0:
            pantalla.blit(self.flecha_izquierda, posicion(-0.043,-0.03,ancho_botón,altura_botón,margin_ratio))
        else:
            pantalla.blit(self.flecha_derecha, posicion(-0.043,-0.03,ancho_botón,altura_botón,margin_ratio))