import pygame
import constantes
import funciones
import sys
from Escribir import Escribir
from Fondo import Fondo
from Boton import Boton
from Escribir import Escribir
from Jugador import Jugador
from Tanque import Tanque

class prueba:

    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game

    def run(self):
        reloj = pygame.time.Clock()
        fondo = Fondo()
        en_menu = True
        ancho_botónt, altura_botónt = 0.25, 0.08

        pos_x_kill = 0.8 - ancho_botónt / 2
        jugador1 = Jugador("prueba 1", Tanque((99, 11, 87)))
        jugador2 = Jugador("prueba 2", Tanque((0, 0, 255)))
        jugador3 = Jugador("prueba 3", Tanque((255, 0, 0)))
        jugador4 = Jugador("prueba 4", Tanque((47, 69, 56)))
        jugador5 = Jugador("prueba 5", Tanque((0, 0, 0)))
        jugador6 = Jugador("prueba 6", Tanque((252, 3, 186)))
        jugadores = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6]
        jugadores_ordenados = sorted(jugadores, key=lambda x: x.kills, reverse=True)
        while en_menu:
            mouse = pygame.mouse.get_pos()
            teclas = pygame.key.get_pressed()
            for event in pygame.event.get():
                if teclas[pygame.K_ESCAPE]:
                    en_menu = False
                    sys.exit()


            fondo.cargar_fondo(self.pantalla, 1)
            # boton jugar
            ancho_botón, altura_botón = 0.75, 0.75

            x_ratio = 0.5 - ancho_botón / 2
            y_ratio = 0.5 - 0.5 * altura_botón
            width_ratio = ancho_botón
            height_ratio = altura_botón
            borde = 50
            hover_color = constantes.CELESTE


            x = x_ratio * constantes.ANCHO_VENTANA
            y = y_ratio * constantes.ALTO_VENTANA
            w = width_ratio * constantes.ANCHO_VENTANA
            h = height_ratio * constantes.ALTO_VENTANA
            pygame.draw.rect(self.pantalla, hover_color, (x, y, w, h), border_radius=borde)
            pos_x = 0.5 - ancho_botónt / 2
            pos_y = 0.25 + 1.5 * altura_botónt
            pos_x_img = 0.4 - ancho_botónt / 2
            Escribir.render_text(self.pantalla, "Puntuacion", (0.64 - ancho_botónt / 2, 0.08 + 1.5 * altura_botónt), 40,constantes.NEGRO, "timesnewroman")
            Escribir.render_text(self.pantalla, "Jugador", (0.5 - ancho_botónt / 2, 0.17 + 1.5 * altura_botónt), 15, constantes.NEGRO, "arial")
            Escribir.render_text(self.pantalla, "Kills", (0.8 - ancho_botónt / 2, 0.17 + 1.5 * altura_botónt), 15,constantes.NEGRO, "arial")


            for player in jugadores_ordenados:
                #self.pantalla.blit(player.tanque.imagen, [pos_x_img, pos_y])
                Escribir.render_text(self.pantalla, player.nombre, (pos_x, pos_y), 15, constantes.NEGRO, "arial")
                Escribir.render_text(self.pantalla, str(player.kills), (pos_x_kill, pos_y),15, constantes.NEGRO, "arial")
                pos_y += 0.09

            pygame.display.flip()
            # Limita los FPS a 60
            reloj.tick(60)