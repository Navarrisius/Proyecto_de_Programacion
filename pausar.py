import pygame
import constantes
from Boton import Boton
import sys
from Escribir import Escribir

class Pausar:
    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game
    def run(self):
        self.pantalla.fill((225, 225, 208))
        ancho_botón, altura_botón = 0.25, 0.08  # Margen de separación entre botones
        margin_ratio = 0.05
        Escribir.render_text(self.pantalla, "En Pausa", (0.35 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.NEGRO, "More Sugar")
        botones = [
            Boton(0.5 - ancho_botón / 2, 0.5 + 1.5 * altura_botón, ancho_botón, altura_botón, "Salir"
                  ,constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)]
        pausado = True
        pygame.display.flip()
        pygame.display.update()
        while pausado:
            teclas = pygame.key.get_pressed()
            reloj = pygame.time.Clock()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botones[0].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                            self.gameStateManager.set_estado('menu')
                            pausado = False 
                            return pausado
                if teclas[pygame.K_ESCAPE]:
                        self.gameStateManager.set_estado('partida')
                        pausado = False
            for boton in botones:
                boton.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)

            pygame.display.flip()
             
        reloj.tick(5)