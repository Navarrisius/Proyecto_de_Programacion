import pygame
import constantes
import funciones
import sys
from Escribir import Escribir
from Fondo import Fondo
from Boton import Boton

class Menu:
    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game
    
        
    def run(self):
        constantes.PANTALLA = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA), pygame.RESIZABLE, pygame.OPENGL)
        en_menu = True
        reloj = pygame.time.Clock()
        fondo = Fondo()
        png_pessi = pygame.image.load('img/pessi.png')
        png_pessi = pygame.transform.scale(png_pessi, (200, 200))
        png_balon_de_hielo = pygame.image.load('img/balon_de_hielo.png')
        png_balon_de_hielo = pygame.transform.scale(png_balon_de_hielo, (120, 120))
        png_balon_de_hielo = pygame.transform.rotate(png_balon_de_hielo, 12)
        ancho_botón, altura_botón = 0.25, 0.08
        margin_ratio = 0.05  # Margen de separación entre botones

        botones = [
            Boton(0.5 - ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio, ancho_botón,
                altura_botón, "Jugar",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
            Boton(0.5 - ancho_botón / 2, 0.5 + 1.5 * altura_botón, ancho_botón, altura_botón, "Ajustes",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
            Boton(0.5 - ancho_botón / 2, 0.5 + 2.5 * altura_botón + margin_ratio, ancho_botón,
                altura_botón, "Controles",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
            Boton(0.5 - ancho_botón / 2, 0.5 + 3.5 * altura_botón + margin_ratio*2, ancho_botón,
                altura_botón, "Salir", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
        ]
        while en_menu:
            mouse = pygame.mouse.get_pos()
            teclas = pygame.key.get_pressed()
            for event in pygame.event.get():
                if teclas[pygame.K_ESCAPE]:
                    en_menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botones[0].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        self.gameStateManager.set_estado('partida')
                        en_menu = False
                    if botones[1].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        self.gameStateManager.set_estado('configurar')
                        en_menu = False
                    if botones[2].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        self.gameStateManager.set_estado('tutorial')
                        en_menu = False
                    if botones[3].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        sys.exit()
            if not en_menu:
                break
            fondo.cargar_fondo(self.pantalla,1)
            self.pantalla.blit(png_pessi, (constantes.ANCHO_VENTANA - 230, constantes.ALTO_VENTANA - 200))
            self.pantalla.blit(png_balon_de_hielo, (constantes.ANCHO_VENTANA - 110, constantes.ALTO_VENTANA - 120))
            # boton jugar
            Escribir.render_text(self.pantalla, "PessiTank", (0.593 - ancho_botón / 2, 0.19 + 1.5 * altura_botón), 85,constantes.NEGRO, "timesnewroman")
            Escribir.render_text(self.pantalla, "PessiTank", (0.597 - ancho_botón / 2, 0.19 + 1.5 * altura_botón), 85, constantes.CELESTE, "timesnewroman")
            png_hielo = pygame.image.load("img/hielo.png").convert_alpha()
            png_hielo = pygame.transform.scale(png_hielo, (320, 220))
            if constantes.ANCHO_VENTANA==800 and constantes.ALTO_VENTANA==800:
                png_hielo = pygame.transform.scale(png_hielo, (220, 150))
            self.pantalla.blit(png_hielo, funciones.posicion(0.50,0.18,ancho_botón,altura_botón,margin_ratio))

            for boton in botones:
                boton.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)

            pygame.display.flip()
            # Limita los FPS a 60
            reloj.tick(60)